from io import RawIOBase, BytesIO
from cbor.CBORStream import CBORStream
from cbor.HexBinStream import HexBinStream
from cbor.MajorType import MajorType


class Decoder:
    def decode_array(self, array: bytes, handler):
        decode_stream = CBORStream(BytesIO(array))
        return self.__decode(decode_stream, handler)

    def decode_stream(self, stream: RawIOBase, handler):
        decode_stream = CBORStream(stream)
        return self.__decode(decode_stream, handler)

    def decode_hex_array(self, array: bytes, handler):
        decode_stream = HexBinStream(BytesIO(array))
        return self.__decode(decode_stream, handler)

    def decode_hex_stream(self, stream: RawIOBase, handler):
        decode_stream = HexBinStream(stream)
        return self.__decode(decode_stream, handler)

    def __decode(self, stream: CBORStream, handler):
        mt = MajorType()
        return mt.run(stream, None)
