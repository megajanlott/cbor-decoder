from cbor.CBORStream import CBORStream
from io import RawIOBase


class Decoder:
    def decode(self, array: bytes):
        pass

    def decode(self, stream: RawIOBase):
        pass

    def decodeHex(self, array: bytes):
        pass

    def decodeHex(self, stream: RawIOBase):
        pass
