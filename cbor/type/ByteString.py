import cbor.CBORStream
import cbor.MajorType
import cbor.State


def int_length(info: bytes):
    return int.from_bytes(info, byteorder='big')


def str_from_bytes(b: bytes):
    return ''.join('{:02x}'.format(x) for x in b);


class ByteString(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        if length == 0:
            handler('')
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
        elif length == 31:
            return [cbor.MajorType.MajorType(), ByteStringInf()]
        return []


class ByteStringInf(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler('')
        return [cbor.MajorType.MajorType(), ByteStringInf()]
