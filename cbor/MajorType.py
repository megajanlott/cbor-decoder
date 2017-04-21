from cbor.CBORStream import CBORStream
from cbor.State import State
from cbor.type.Array import ArrayInfo
from cbor.type.ByteString import ByteString
from cbor.type.Map import MapInfo
from cbor.type.Tag import TagInfo
from cbor.type.TextString import TextString
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
        elif t == 2:
            return ByteString()
        elif t == 3:
            return TextString()
        elif t == 4:
            return ArrayInfo()
        elif t == 5:
            return MapInfo()
        elif t == 6:
            return TagInfo()

        return
