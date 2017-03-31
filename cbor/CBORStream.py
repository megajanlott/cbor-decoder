from io import RawIOBase


class CBORStream:
    def __init__(self, stream: RawIOBase):
        self.stream = stream
        self.peeked = b''

    def peek(self, n: int = 1):
        if len(self.peeked) >= n:
            return self.peeked[:n]
        self.peeked += self._read(n - len(self.peeked))
        return self.peeked

    def read(self, n: int = 1):
        output = bytes()
        if len(self.peeked) > 0:
            output = self.peeked
            if n >= len(self.peeked):
                n -= len(self.peeked)
            self.peeked = b''
        output += self._read(n)
        return output

    def _read(self, n: int):
        return bytes(self.stream.read(n))
