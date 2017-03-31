class CBORStream:
    def __init__(self, stream):
        self.stream = stream

    def peek(self, n=1):
        pass

    def read(self, n=1):
        return self.stream.read(n)
