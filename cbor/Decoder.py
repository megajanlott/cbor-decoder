from cbor.CBORStream import CBORStream
from io import RawIOBase


class Decoder:
    def decode(self, array: bytes):
        pass

    def decode(self, stream: RawIOBase):
        pass

    def decode_hex(self, array: bytes):
        pass

    def decode_hex(self, stream: RawIOBase):
        pass
