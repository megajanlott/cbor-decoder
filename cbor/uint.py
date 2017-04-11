from cbor.CBORStream import CBORStream
from cbor.State import State


class UIntInfo(State):
    def run(self, stream: CBORStream, handler):
        return

    def type(self):
        raise NotImplementedError


class UIntRead(State):
    def __init__(self, n):
        self.n = n

    def run(self, stream: CBORStream, handler):
        return

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
