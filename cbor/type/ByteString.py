import cbor.CBORStream
import cbor.MajorType
import cbor.State


def int_length(info: bytes):
    return int.from_bytes(info, byteorder='big')


class ByteString(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        if length == 0:
            handler('')
        elif length < 24:
            handler(stream.read(length))
        elif length == 24:
            handler(stream.read(int_length(stream.read(1))))
        elif length == 25:
            handler(stream.read(int_length(stream.read(2))))
        elif length == 26:
            handler(stream.read(int_length(stream.read(3))))
        elif length == 27:
            handler(stream.read(int_length(stream.read(4))))
        elif length == 31:
            return [cbor.MajorType.MajorType(), ByteStringInf()]
        return []


class ByteStringInf(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler('')
        return [cbor.MajorType.MajorType(), ByteStringInf()]
