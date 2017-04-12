from cbor.CBORStream import CBORStream
from cbor.MajorType import MajorType
from cbor.State import State


class ArrayInfo(State):

    def run(self, stream: CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        handler('[')
        if length < 24:
            return [MajorType(), ArrayRead(length, True)]
        elif length == 24:
            return [ArrayLen(1)]
        elif length == 25:
            return [ArrayLen(2)]
        elif length == 26:
            return [ArrayLen(4)]
        elif length == 27:
            return [ArrayLen(8)]
        elif length == 31:
            return [MajorType(), ArrayInf(True)]
        return []


class ArrayRead(State):

    def __init__(self, n: int, first: bool = False):
        self.n = n
        self.first = first

    def run(self, stream: CBORStream, handler):
        if self.n > 0:
            if not self.first:
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

    def __init__(self, first: bool = False):
        self.first = first

    def run(self, stream: CBORStream, handler):
        if not self.first:
            handler(',')
        return [MajorType(), ArrayInf()]
