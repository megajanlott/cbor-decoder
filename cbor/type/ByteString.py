import cbor.CBORStream
import cbor.MajorType
import cbor.State


class ByteString(cbor.State.State):

    def run(self, stream: cbor.CBORStream.CBORStream, handler):
        info = stream.read(1)
        length = ord(info) & 0b00011111
        if length == 0:
            handler('')
        elif length < 24:
            handler(stream.read(length))
        elif length == 24:
            pass
        elif length == 25:
            pass
        elif length == 26:
            pass
        elif length == 27:
            pass
        elif length == 31:
            pass
        return []