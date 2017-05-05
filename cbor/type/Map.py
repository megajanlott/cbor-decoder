import cbor.CBORStream
import cbor.MajorType
import cbor.State


class MapInfo(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        handler('{')
        if length == 0:
            handler('}')
        elif length < 24:
            return [MapReadValue(length), cbor.MajorType.MajorType()]
        elif length == 24:
            return [MapLen(1)]
        elif length == 25:
            return [MapLen(2)]
        elif length == 26:
            return [MapLen(4)]
        elif length == 27:
            return [MapLen(8)]
        elif length == 31:
            return [MapInfValue(), cbor.MajorType.MajorType()]
        return []


class MapLen(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(self.n)
        length = int.from_bytes(info, byteorder='big')
        return [MapReadValue(length), cbor.MajorType.MajorType()]


class MapReadKey(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        if self.n == 0:
            handler('}')
            return []
        if self.n > 0:
            handler(',')
        return [MapReadValue(self.n), cbor.MajorType.MajorType()]


class MapReadValue(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n: int):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler(':')
        return [MapReadKey(self.n-1), cbor.MajorType.MajorType()]


class MapInfKey(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        if stream.peek(1) != b'\xff':
            handler(',')
        return [MapInfValue(), cbor.MajorType.MajorType()]


class MapInfValue(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        handler(':')
        return [MapInfKey(), cbor.MajorType.MajorType()]


def MapInfClose(handler):
    handler('}')
