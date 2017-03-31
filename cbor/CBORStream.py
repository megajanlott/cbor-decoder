from io import RawIOBase


class CBORStream:
    def __init__(self, stream: RawIOBase):
        self.stream = stream
        self.peeked = None
        self.peek_length = 1

    def peek1(self):
        self.peeked = self.read(1)
        return self.peeked

    def read(self, n: int = 1):
        output = bytes()
        if self.peeked is not None:
            output = bytes(self.peeked)
            self.peeked = None
            if n >= self.peek_length:
                n -= self.peek_length
        output += bytes(self.stream.read(n))
        return output
