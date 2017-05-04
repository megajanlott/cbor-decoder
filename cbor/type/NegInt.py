import cbor.CBORStream
import cbor.State


class NegIntInfo(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111

        if length < 24:
            handler(str(-1 - length))
            return []
        elif length == 24:
            return [NegIntRead(1)]
        elif length == 25:
            return [NegIntRead(2)]
        elif length == 26:
            return [NegIntRead(4)]
        elif length == 27:
            return [NegIntRead(8)]
        return []


class NegIntRead(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        int_data = stream.read(self.n)
        int_value = -1 - int.from_bytes(int_data, byteorder='big')
        handler(str(int_value))
        return []
