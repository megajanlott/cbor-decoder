# imports
import cbor.CBORStream
import cbor.State
import struct

# constants
ADDITIONAL_DATA_LENGTH_MASK = 0b00011111
NEXT_1BYTE = 24
NEXT_2BYTE = 25
NEXT_4BYTE = 26
NEXT_8BYTE = 27


def decode_uint(data, length):
    if length == 1:
        return struct.unpack('B', data)[0]
    elif length == 2:
        numbers = struct.unpack('BB', data)
        return (256 * numbers[0] + numbers[1])
    elif length == 4:
        numbers = struct.unpack('BBBB', data)
        return (16777216 * numbers[0] + 65536 * numbers[1] + 256 * numbers[2] + numbers[3])
    elif length == 8:
        numbers = struct.unpack('BBBBBBBB', data)
        return (72057594037927936 * numbers[0] + 281474976710656 * numbers[1] + 1099511627776 * numbers[2] + 4294967296 * numbers[3] + \
        16777216 * numbers[4] + 65536 * numbers[5] + 256 * numbers[6] + numbers[7])


class UIntRead(cbor.State.State):
    def __init__(self, n):
        self.n = n

    def run(self, stream: cbor.CBORStream.CBORStream, handler=None):
        current_data = stream.read(self.n)

        data = decode_uint(current_data, self.n)
        return data

    def type(self):
        raise NotImplementedError


class UIntInfo(cbor.State.State):
    def run(self, stream: cbor.CBORStream.CBORStream, handler=None):

        current_data = stream.read(1)
        current_int = struct.unpack('B', current_data)[0]
        last_five_bits = (current_int & ADDITIONAL_DATA_LENGTH_MASK)

        if last_five_bits < 24:
            return last_five_bits
        elif last_five_bits == NEXT_1BYTE:
            return UIntRead(1).run(stream)
        elif last_five_bits == NEXT_2BYTE:
            return UIntRead(2).run(stream)
        elif last_five_bits == NEXT_4BYTE:
            return UIntRead(4).run(stream)
        elif last_five_bits == NEXT_8BYTE:
            return UIntRead(8).run(stream)
        else:
            return None

    def type(self):
        raise NotImplementedError