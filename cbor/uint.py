# imports
from CBORStream import CBORStream
from State import State
import struct

# constants
ADDITIONAL_DATA_LENGTH_MASK = 0b00011111
NEXT_1BYTE = 24
NEXT_2BYTE = 25
NEXT_4BYTE = 26
NEXT_8BYTE = 27


def decode_uint(data, length):
    print(data)
    if length == 1:
        return struct.unpack('B', data)[0]
    elif length == 2:
        numbers = struct.unpack('BB', data)
        return (256 * numbers[0] + numbers[1])
    elif length == 4:
        numbers = struct.unpack('BBBB', bytes)
        return (16777216 * numbers[0] + 65536 * numbers[1] + 256 * numbers[2] + numbers[3])
    elif length == 8:
        numbers = struct.unpack('BBBBBBBB', bytes)
        return (72057594037927936 * numbers[0] + 281474976710656 * numbers[1] + 1099511627776 * numbers[2] + 4294967296 * numbers[3] + \
        16777216 * numbers[4] + 65536 * numbers[5] + 256 * numbers[6] + numbers[7])


class UIntRead(State):
    def __init__(self, n):
        self.n = n
        self.run(CBORStream)

    def run(self, stream: CBORStream, handler=None):
        current_data = bytes([1,244])  # must be changed to read from stream

        data = decode_uint(current_data, self.n)
        print(data)
        # handler(data)
        return None

    def type(self):
        raise NotImplementedError


class UIntInfo(State):
    def run(self, stream: CBORStream, handler=None):

        current_data = bytes([25])  # must be changed to read from stream
        current_int = struct.unpack('B', current_data)[0]  # bytes to int conversation
        last_five_bits = (current_int & ADDITIONAL_DATA_LENGTH_MASK)

        if last_five_bits < 24:
            print('number itself')
            print(last_five_bits)
            # handler(last_five_bits)
            return None
        elif last_five_bits == NEXT_1BYTE:
            print('1byte')
            return UIntRead(1)
        elif last_five_bits == NEXT_2BYTE:
            print('2byte')
            return UIntRead(2)
        elif last_five_bits == NEXT_4BYTE:
            print('4byte')
            return UIntRead(4)
        elif last_five_bits == NEXT_8BYTE:
            print('8byte')
            return UIntRead(8)
        else:
            return None

    def type(self):
        raise NotImplementedError


UInt = UIntInfo()
UInt.run(CBORStream)
