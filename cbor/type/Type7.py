import cbor.CBORStream
import cbor.MajorType
import cbor.State
import struct

ADDITIONAL_INFORMATION_MASK = 0b00011111

simple_value_next = 24
float_2byte_next = 25
float_4byte_next = 26
float_8byte_next = 27
inf_end = 31


def decode_simple_value(value):
    if value <= 19:
        # unassigned
        return []
    elif value == 20:
        return 'False'
    elif value == 21:
        return 'True'
    elif value == 22:
        return 'Null'
    elif value == 23:
        # undefined
        return []
    elif ((value >= 24) & (value <= 31)):
        # reserved
        return []
    else:
        # unassigned
        return []


class Type7Info(cbor.State.State):

    def run(self, stream: cbor.CBORStream, handler):
        current = stream.read(1)
        current = int.from_bytes(current, byteorder='big')

        add_inf = (current & ADDITIONAL_INFORMATION_MASK)

        if add_inf < 24:
            simple_value = decode_simple_value(add_inf)
            handler(simple_value)
            return []
        elif add_inf == simple_value_next:
            return [Type7Read()]
        elif add_inf == float_2byte_next:
            return [FloatRead(2)]
        elif add_inf == float_4byte_next:
            return [FloatRead(4)]
        elif add_inf == float_8byte_next:
            return [FloatRead(8)]
        elif add_inf == inf_end:
            return ['break']


class Type7Read(cbor.State.State):

    def run(self, stream: cbor.CBORStream, handler):
        value = stream.read(1)
        value = int.from_bytes(value, byteorder='big')

        simple_value = decode_simple_value(value)
        handler(simple_value)
        #self.none = None
        return []


class FloatRead(cbor.State.State):

    def __eq__(self, other):
        return self.n == other.n

    def __init__(self, n):
        self.n = n

    def run(self, stream: cbor.CBORStream, handler):
        #value = stream.read(self.n)
        data = []
        for i in range(0,self.n):
            current = stream.read(1)
            current = int.from_bytes(current, byteorder='big')
            data.append(current)
        if self.n == 2:
            value = struct.pack('2B', *data)
            float_value = struct.unpack('e', value)
        if self.n == 4:
            value = struct.pack('4B', *data)
            float_value = struct.unpack('>f', value)
        if self.n == 8:
            value = struct.pack('8B', *data)
            float_value = struct.unpack('d', value)
        handler(str(float_value))
        return []