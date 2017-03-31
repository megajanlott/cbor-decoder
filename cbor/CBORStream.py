from io import RawIOBase


class CBORStream:
    def __init__(self, stream: RawIOBase):
        self.stream = stream

    def peek(self, n: int = 1):
        pass

    def read(self, n: int = 1):
        return self.stream.read(n)
