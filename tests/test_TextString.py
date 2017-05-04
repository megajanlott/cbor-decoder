from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.TextString import TextString
from tests.MockHandler import MockHandler


def test_run_text_string_probe():
    data = CBORStream(BytesIO(bytes([0b01100001])))
    assert type(MajorType().run(data, None)) == TextString


def test_run_text_string_read():
    handler = MockHandler()
    encoded_data = bytearray.fromhex('60')
    data = CBORStream(BytesIO(encoded_data))
    stack = TextString().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('\"\"')


def test_run_text_string_read_a():
    handler = MockHandler()
    encoded_data = bytearray.fromhex('6161')
    data = CBORStream(BytesIO(encoded_data))
    stack = TextString().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('\"a\"')


def test_run_text_string_read_ietf():
    handler = MockHandler()
    encoded_data = bytearray.fromhex('6449455446')
    data = CBORStream(BytesIO(encoded_data))
    stack = TextString().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('\"IETF\"')
