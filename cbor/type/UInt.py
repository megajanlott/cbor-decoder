import cbor.CBORStream
import cbor.State


class UIntInfo(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111

        if length < 24:
            handler(str(length))
            return []
        elif length == 24:
            return [UIntRead(1)]
        elif length == 25:
            return [UIntRead(2)]
        elif length == 26:
            return [UIntRead(4)]
        elif length == 27:
            return [UIntRead(8)]
        return []


class UIntRead(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        int_data = stream.read(self.n)
        int_value = int.from_bytes(int_data, byteorder='big')
        handler(str(int_value))
        return []
