from io import RawIOBase, BytesIO
from cbor.CBORStream import CBORStream
from cbor.HexBinStream import HexBinStream


class Decoder:
    def decode_array(self, array: bytes):
        decode_stream = CBORStream(BytesIO(array))
        return self.__decode(decode_stream)

    def decode_stream(self, stream: RawIOBase):
        decode_stream = CBORStream(stream)
        return self.__decode(decode_stream)

    def decode_hex_array(self, array: bytes):
        decode_stream = HexBinStream(BytesIO(array))
        return self.__decode(decode_stream)

    def decode_hex_stream(self, stream: RawIOBase):
        decode_stream = HexBinStream(stream)
        return self.__decode(decode_stream)

    def __decode(self, stream: CBORStream):
        stream.peek()
