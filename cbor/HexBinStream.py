from cbor.CBORStream import CBORStream
from binascii import unhexlify


class HexBinStream(CBORStream):
    def __init__(self, stream):
        super().__init__(stream)

    def peek(self, n=1):
        pass

    def read(self, n=1):
        in_hex = self.stream.read(2*n)
        return unhexlify(in_hex)
