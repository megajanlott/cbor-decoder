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
    if length == 1:
        return ord(struct.pack('B', data))
    elif length == 2:
        return ord(struct.pack('BB', data))
    elif length == 4:
        return ord(struct.pack('BBBB', data))
    elif length == 8:
        return ord(struct.pack('BBBBBBBB', data))


class UIntRead(State):
    def __init__(self, n):
        self.n = n
        self.run(CBORStream)

    def run(self, stream: CBORStream, handler=None):
        current_data = '01010101'  # must be changed to read from stream
        current_int = int(current_data, 2)  # byte to int conversation

        data = decode_uint(current_int, self.n)
        # handler(data)
        print(data)
        return None

    def type(self):
        raise NotImplementedError


class UIntInfo(State):
    def run(self, stream: CBORStream, handler=None):

        current_data = '000011000'  # must be changed to read from stream
        current_int = int(current_data, 2)  # byte to int conversation
        last_five_bits = (current_int & ADDITIONAL_DATA_LENGTH_MASK)

        if last_five_bits < 24:
            data = decode_uint(last_five_bits)
            # handler(data)
            print('number itself')
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
