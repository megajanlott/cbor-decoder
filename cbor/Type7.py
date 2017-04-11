from cbor.CBORStream import CBORStream
from cbor.State import State

ADDITIONAL_INFORMATION_MASK = 0b00011111

simple_value_next = 24
float_2byte_next = 25
float_4byte_next = 26
float_8byte_next = 27
inf_end = 31


def decode_simple_value(value):
    if value <=19:
        #unassigned
        return 'pass'
    elif value == 20:
        return 'False'
    elif value == 21:
        return 'True'
    elif value == 22:
        return 'Null'
    elif value == 23:
        #undefined
        return 'pass'
    elif ((value>=24) & (value<=31)):
        #reserved
        return 'pass'
    else:
        #unassigned
        return 'pass'

class Type7Info(State):

    def run(self, stream: CBORStream, handler = None):
        current = stream.read(1)
        current = int.from_bytes(current, byteorder='big')

        add_inf = (current & ADDITIONAL_INFORMATION_MASK)

        if add_inf < 24:
            simple_value = decode_simple_value(add_inf)
            handler(simple_value)
            return None
        elif add_inf == simple_value_next:
            return Type7Read
        elif add_inf == float_2byte_next:
            return FloatRead(2)
        elif add_inf == float_4byte_next:
            return FloatRead(4)
        elif add_inf == float_8byte_next:
            return FloatRead(8)
        elif add_inf == inf_end:
            return 'break'

    def type(self):
        raise NotImplementedError


class Type7Read(State):

    def run(self, stream: CBORStream, handler = None):
        value = stream.read(1)
        value = int.from_bytes(value, byteorder='big')

        simple_value = decode_simple_value(value)
        handler(simple_value)
        return None

    def type(self):
        raise NotImplementedError


class FloatRead(State):

    def __init__(self, n):
        self.bytes_to_read = n

    def run(self, stream: CBORStream, handler = None):
        value = stream.read(self.bytes_to_read)
        int_value = int.from_bytes(value,byteorder='big')
        float_value = float(int_value,0)
        handler(float_value)
        return None

    def type(self):
        raise NotImplementedError