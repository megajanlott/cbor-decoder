import cbor.CBORStream
import cbor.MajorType
import cbor.State


def int_length(info: bytes):
    return int.from_bytes(info, byteorder='big')


def str_from_bytes(info: bytes):
    return ''.join('{:02x}'.format(x) for x in info)


class ByteString(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        handler('\"')
        if length == 31:
            return [cbor.MajorType.MajorType(), ByteStringInf()]
        elif length < 24:
            data = stream.read(length)
            handler(str_from_bytes(data))
        elif length == 24:
            data = stream.read(int_length(stream.read(1)))
            handler(str_from_bytes(data))
        elif length == 25:
            data = stream.read(int_length(stream.read(2)))
            handler(str_from_bytes(data))
        elif length == 26:
            data = stream.read(int_length(stream.read(3)))
            handler(str_from_bytes(data))
        elif length == 27:
            data = stream.read(int_length(stream.read(4)))
            handler(str_from_bytes(data))
        elif length == 0:
            handler('')
        handler('\"')
        return []


class ByteStringInf(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler('')
        return [ByteStringInf(), cbor.MajorType.MajorType()]


def ByteStringInfClose(handler):
    handler('\"')
