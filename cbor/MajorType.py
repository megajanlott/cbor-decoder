from cbor.CBORStream import CBORStream
from cbor.State import State
from cbor.type.UInt import UIntInfo
from cbor.type.Neg_Int import NegIntInfo

MAJOR_TYPE_MASK = 0b11100000
MAJOR_TYPE_SIZE = 3


class MajorType(State):
    def run(self, stream: CBORStream, handler):
        current = stream.peek(1)

        t = (ord(current) & MAJOR_TYPE_MASK) >> (8 - MAJOR_TYPE_SIZE)

        if t == 0:
            # should return the proper major type instance
            return UIntInfo()
        elif t == 1:
            # should return the proper major type instance
            return NegIntInfo()
        elif t == 4:
            return
