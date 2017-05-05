import cbor.CBORStream
import cbor.MajorType
import cbor.State


def int_length(info: bytes):
    return int.from_bytes(info, byteorder='big')


def decode_utf_bytes(info: bytes):
    return info.decode("utf-8")


class TextString(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        handler('\"')
        if length == 31:
            return [cbor.MajorType.MajorType(), TextStringInf()]
        elif length < 24:
            handler(decode_utf_bytes(stream.read(length)))
        elif length == 24:
            handler(decode_utf_bytes(stream.read(int_length(stream.read(1)))))
        elif length == 25:
            handler(decode_utf_bytes(stream.read(int_length(stream.read(2)))))
        elif length == 26:
            handler(decode_utf_bytes(stream.read(int_length(stream.read(3)))))
        elif length == 27:
            handler(decode_utf_bytes(stream.read(int_length(stream.read(4)))))
        elif length == 0:
            handler('')
        handler('\"')
        return []


class TextStringInf(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler('')
        return [TextStringInf(), cbor.MajorType.MajorType()]


def TextStringInfClose(handler):
    handler('\"')
