from cbor.CBORStream import CBORStream
from cbor.MajorType import MajorType


class ArrayInfo(MajorType):

    def __init__(self):
        pass

    def run(self, stream: CBORStream, handler):
        pass

    def type(self):
        pass


class ArrayRead(MajorType):

    def __init__(self, n: int):
        self.n = n
        pass

    def run(self, stream: CBORStream, handler):
        pass

    def type(self):
        pass


class ArrayLen(MajorType):

    def __init__(self, n: int):
        self.n = n
        pass

    def run(self, stream: CBORStream, handler):
        pass

    def type(self):
        pass


class ArrayInf(MajorType):

    def __init__(self):
        pass

    def run(self, stream: CBORStream, handler):
        pass

    def type(self):
        pass
