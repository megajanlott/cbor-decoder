from cbor.CBORStream import CBORStream
from cbor.State import State

MAJOR_TYPE_MASK = 0b11100000
MAJOR_TYPE_SIZE = 3


class MajorType(State):
    def run(self, stream: CBORStream, handler):
        current = stream.peek(1)

        t = (ord(current) & MAJOR_TYPE_MASK) >> (8 - MAJOR_TYPE_SIZE)

        if t == 0:
            return 'Unsigned int'
        elif t == 1:
            return 'Negative int'

        return 'No type'

    def type(self):
        raise NotImplementedError
