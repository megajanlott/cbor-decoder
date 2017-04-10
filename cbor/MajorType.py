from cbor.CBORStream import CBORStream
from cbor.State import State

MAJOR_TYPE_MASK = 0b11100000
MAJOR_TYPE_SIZE = 3


class MajorType(State):
    def run(self, stream: CBORStream, handler):
        current = stream.peek(1)

        t = (ord(current) & MAJOR_TYPE_MASK) >> (8 - MAJOR_TYPE_SIZE)

        if t == 0:
            # should return the proper major type instance
            return 'Unsigned int'
        elif t == 1:
            # should return the proper major type instance
            return 'Negative int'

        return 'No type'

    def type(self):
        raise NotImplementedError
