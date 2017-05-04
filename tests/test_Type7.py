from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from tests.MockHandler import MockHandler

from cbor.type.Type7 import *

#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


def ignore_handler(v):
    return

def test_run_type7_probe():
    data = CBORStream(BytesIO(bytes([0b11100001])))
    assert type(MajorType().run(data, None)) == Type7Info

def test_Type7Info_True():
    handler = MockHandler()
    data = CBORStream(BytesIO(bytes([0b00010101])))
    stack = Type7Info().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('True')

def test_Type7Info_False():
    handler = MockHandler()
    data = CBORStream(BytesIO(bytes([0b00010100])))
    stack = Type7Info().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('False')

def test_Type7Info_Null():
    handler = MockHandler()
    data = CBORStream(BytesIO(bytes([0b00010110])))
    stack = Type7Info().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('Null')

def test_Type7Info_simple_value_next():
    data = CBORStream(BytesIO(bytes([0b11111000])))

    stack = Type7Info().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == Type7Read

def test_Type7Info_float_2byte_next():
    data = CBORStream(BytesIO(bytes([0b11111001])))
    stack = Type7Info().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == FloatRead
    assert stack[0] == FloatRead(2)

def test_Type7Info_float_4byte_next():
    data = CBORStream(BytesIO(bytes([0b11111010])))
    stack = Type7Info().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == FloatRead
    assert stack[0] == FloatRead(4)

def test_Type7Info_float_8byte_next():
    data = CBORStream(BytesIO(bytes([0b11111011])))
    stack = Type7Info().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == FloatRead
    assert stack[0] == FloatRead(8)

def test_Type7Info_inf_end():
    data = CBORStream(BytesIO(bytes([0b11111111])))
    stack = Type7Info().run(data, ignore_handler)
    assert len(stack) == 1
    assert stack[0] == 'break'

def test_Type7Info_inf_end_vmi():
    data = CBORStream(BytesIO(bytes([0b11111001])))
    result = Type7Info().run(data)
    assert type(result) == FloatRead
    assert result.bytes_to_read == 2

def test_Type7Read_pass():
    data = CBORStream(BytesIO(bytes([0b00000110])))
    stack = Type7Read().run(data, ignore_handler)
    assert len(stack) == 0

def test_FloatRead():
    handler = MockHandler()
    data = CBORStream(BytesIO(bytes([0b01000001, 0b11001011, 0b01100000, 0b01000010])))
    stack = FloatRead(4).run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('25.422000885009766')