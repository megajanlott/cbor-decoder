from binascii import unhexlify
from cbor.CBORStream import CBORStream
from io import RawIOBase


class HexBinStream(CBORStream):
    def __init__(self, stream: RawIOBase):
        super().__init__(stream)
        self.peek_length = 2

    def read(self, n: int = 1):
        in_hex = self.stream.read(2*n)
        return bytes(unhexlify(in_hex))
