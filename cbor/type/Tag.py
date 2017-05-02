import cbor.CBORStream
import cbor.MajorType
import cbor.State


class TagInfo(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        if length == 24:
            return [TagRead(1)]
        elif length == 25:
            return [TagRead(2)]
        elif length == 26:
            return [TagRead(4)]
        elif length == 27:
            return [TagRead(8)]
        return [cbor.MajorType.MajorType()]


class TagRead(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        stream.read(self.n)
        return [cbor.MajorType.MajorType()]
