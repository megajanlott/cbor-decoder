from cbor.CBORStream import CBORStream
from cbor.MajorType import MajorType
from cbor.State import State


class ArrayInfo(State):

    def run(self, stream: CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        handler('[')
        if length < 24:
            return [MajorType(), ArrayRead(length)]
        elif length == 24:
            return [ArrayLen(1)]
        elif length == 25:
            return [ArrayLen(2)]
        elif length == 26:
            return [ArrayLen(4)]
        elif length == 27:
            return [ArrayLen(8)]
        elif length == 31:
            return [MajorType(), ArrayInf()]
        return []


class ArrayRead(State):

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: CBORStream, handler):
        if self.n > 1:
            handler(',')
            return [MajorType(), ArrayRead(self.n - 1)]
        handler(']')
        return []


class ArrayLen(State):

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: CBORStream, handler):
        info = stream.read(self.n)
        length = int.from_bytes(info, byteorder='big')
        return [MajorType(), ArrayRead(length)]


class ArrayInf(State):

    def run(self, stream: CBORStream, handler):
        handler(',')
        return [MajorType(), ArrayInf()]
