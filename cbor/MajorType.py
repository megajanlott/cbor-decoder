from cbor.CBORStream import CBORStream
from cbor.State import State
from cbor.type.ByteString import ByteString
from cbor.type.TextString import TextString
from cbor.type.Array import ArrayInfo
from cbor.type.Map import MapInfo

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
        elif t == 2:
            return ByteString()
        elif t == 3:
            return TextString()
        elif t == 4:
            return ArrayInfo()
        elif t == 5:
            return MapInfo()

        return
