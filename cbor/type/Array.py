import cbor.CBORStream
import cbor.MajorType
import cbor.State


class ArrayInfo(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        handler('[')
        if length == 0:
            handler(']')
        elif length < 24:
            return [cbor.MajorType.MajorType(), ArrayRead(length)]
        elif length == 24:
            return [ArrayLen(1)]
        elif length == 25:
            return [ArrayLen(2)]
        elif length == 26:
            return [ArrayLen(4)]
        elif length == 27:
            return [ArrayLen(8)]
        elif length == 31:
            return [cbor.MajorType.MajorType(), ArrayInf()]
        return []


class ArrayRead(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        if self.n > 1:
            handler(',')
            return [cbor.MajorType.MajorType(), ArrayRead(self.n - 1)]
        handler(']')
        return []


class ArrayLen(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(self.n)
        length = int.from_bytes(info, byteorder='big')
        return [cbor.MajorType.MajorType(), ArrayRead(length)]


class ArrayInf(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler(',')
        return [cbor.MajorType.MajorType(), ArrayInf()]
