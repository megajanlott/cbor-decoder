from cbor.CBORStream import CBORStream
from cbor.State import State
from examples.simple import printer

MAJOR_TYPE_MASK = 0b11100000
ADDITIONAL_DATA_LENGTH_MASK = 0b00011111
MAJOR_TYPE_SIZE = 3

class UIntInfo(State):
    def run(self, stream: CBORStream, handler):
        current_value = stream.peek(1)
        last_five_bits = ord(current_value) & ADDITIONAL_DATA_LENGTH_MASK
        if last_five_bits < 24:
            printer(current_value)
            return []
        elif last_five_bits == 24:
            additional_bytes = 1
        elif last_five_bits == 25:
            additional_bytes = 2
        elif last_five_bits == 26:
            additional_bytes = 4
        elif last_five_bits == 27:
            additional_bytes = 8

        return UIntRead(additional_bytes)

    def type(self):
        raise NotImplementedError


class UIntRead(State):
    def __init__(self, n):
        self.n = n

    def run(self, stream: CBORStream, handler):
        readed = stream.peek(self.n)
        printer(readed)
        return []

    def type(self):
        raise NotImplementedError

# import struct
# import sys
#
# def int_to_cbor_uint(in_bytes):
#     if in_bytes >= 0x0:#0
#         if in_bytes <= 0x17:#23
#             return struct.pack('B', in_bytes)
#         if in_bytes <= 0x0ff:#255
#             return struct.pack('BB', 24, in_bytes)
#         if in_bytes <= 0x0ffff:#65535
#             return struct.pack('!BH', 25, in_bytes)
#         if in_bytes <= 0x0ffffffff:#4294967295
#             return struct.pack('!BI', 26, in_bytes)
#         if in_bytes <= 0x0ffffffffffffffff:#18446744073709551615
#             return struct.pack('!BQ', 27, in_bytes)
#
# fp = open('workfile', 'wb')
# fp.write(int_to_cbor_uint(int(sys.argv[1])))
#
# fp = open('workfile', 'rb')
# readed_byte = fp.read(1)
#
# first_byte = ord(readed_byte)
#
# def construct_uint(first_byte):
#     if first_byte == 24:
#         number = fp.read(1)
#         print(ord(number))
#         return number
#     if first_byte == 25:
#         bytes = fp.read(2)
#         numbers = struct.unpack('BB', bytes)
#         res = 256 * numbers[0] + numbers[1]
#         print(res)
#         return res
#     if first_byte == 26:
#         bytes = fp.read(4)
#         numbers = struct.unpack('BBBB', bytes)
#         res = 16777216 * numbers[0] + 65536 * numbers[1] + 256 * numbers[2] + numbers[3]
#         print(res)
#         return res
#     if first_byte == 27:
#         bytes = fp.read(8)
#         numbers = struct.unpack('BBBBBBBB', bytes)
#         res = 72057594037927936 * numbers[0] + 281474976710656 * numbers[1] + 1099511627776 * numbers[2] + 4294967296 * numbers[3] + \
#               16777216 * numbers[4] + 65536 * numbers[5] + 256 * numbers[6] + numbers[7]
#         print(res)
#         return res
#
# construct_uint(first_byte)
