from cbor.CBORStream import CBORStream
from cbor.State import State


class ArrayInfo(State):

    def run(self, stream: CBORStream, handler):
        pass


class ArrayRead(State):

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: CBORStream, handler):
        pass


class ArrayLen(State):

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: CBORStream, handler):
        pass


class ArrayInf(State):

    def run(self, stream: CBORStream, handler):
        pass
