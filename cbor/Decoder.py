from cbor.CBORStream import CBORStream
from cbor.HexBinStream import HexBinStream
from io import RawIOBase, BytesIO


class Decoder:
    def decode(self, array: bytes):
        decode_stream = CBORStream(BytesIO(array))
        return self.__decode(decode_stream)

    def decode(self, stream: RawIOBase):
        decode_stream = CBORStream(stream)
        return self.__decode(decode_stream)

    def decode_hex(self, array: bytes):
        decode_stream = HexBinStream(BytesIO(array))
        return self.__decode(decode_stream)

    def decode_hex(self, stream: RawIOBase):
        decode_stream = HexBinStream(stream)
        return self.__decode(decode_stream)

    def __decode(self, stream: CBORStream):
        pass
