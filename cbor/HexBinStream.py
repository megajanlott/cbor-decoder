from binascii import unhexlify
from cbor.CBORStream import CBORStream
from io import RawIOBase


class HexBinStream(CBORStream):
    def __init__(self, stream: RawIOBase):
        super().__init__(stream)

    def _read(self, n: int):
        in_hex = self.stream.read(2*n)
        return unhexlify(in_hex)
