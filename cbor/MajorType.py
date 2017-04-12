from cbor.CBORStream import CBORStream
from cbor.State import State
from cbor.type.Array import ArrayInf

MAJOR_TYPE_MASK = 0b11100000
MAJOR_TYPE_SIZE = 3


class MajorType(State):
    def run(self, stream: CBORStream, handler):
        current = stream.peek(1)

        t = (ord(current) & MAJOR_TYPE_MASK) >> (8 - MAJOR_TYPE_SIZE)

        if t == 0:
            # should return the proper major type instance
            return
        elif t == 1:
            # should return the proper major type instance
            return
        elif t == 4:
            return ArrayInf()

        return

    def type(self):
        raise NotImplementedError
