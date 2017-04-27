from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.ByteString import ByteString
from tests.MockHandler import MockHandler


def test_run_byte_string_probe():
    data = CBORStream(BytesIO(bytes([0b01000001])))
    assert type(MajorType().run(data, None)) == ByteString


def test_run_byte_string_read():
    handler = MockHandler()
    encoded_data = bytearray.fromhex('40')
    data = CBORStream(BytesIO(encoded_data))
    stack = ByteString().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('')


def test_run_byte_string_read_value():
    handler = MockHandler()
    encoded_data = bytearray.fromhex('4401020304')
    data = CBORStream(BytesIO(encoded_data))
    stack = ByteString().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('01020304')
