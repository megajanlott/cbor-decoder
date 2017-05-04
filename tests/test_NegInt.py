from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.NegInt import NegIntInfo
from tests.MockHandler import MockHandler


def ignore_handler(v):
    return


def test_run_negint_probe():
    data = CBORStream(BytesIO(bytes([0b00100001])))
    assert type(MajorType().run(data, None)) == NegIntInfo


def test_run_negint_same_byte():
    handler = MockHandler()

    # NegInt length lower than 24.
    data = CBORStream(BytesIO(bytes([0b00110111])))
    stack = NegIntInfo().run(data, handler.handler)
    handler.assert_data('-24')


def test_run_negint_multibyte():
    handler = MockHandler()

    # NegInt length on 1 byte.
    data = CBORStream(BytesIO(bytes([
        0b00111000, 0b11100101
    ])))
    stack = NegIntInfo().run(data, ignore_handler)
    assert len(stack) == 1
    stack2 = stack[0].run(data, handler.handler)
    assert len(stack2) == 0
    handler.assert_data('-230')

    # NegInt length on 2 byte.
    data = CBORStream(BytesIO(bytes([
        0b00111001, 0b11100101, 0b10101010
    ])))
    stack = NegIntInfo().run(data, ignore_handler)
    assert len(stack) == 1
    stack2 = stack[0].run(data, handler.handler)
    assert len(stack2) == 0
    handler.assert_data('-58795')

    # NegInt length on 4 byte.
    data = CBORStream(BytesIO(bytes([
        0b00111010, 0b11100101, 0b00100101, 0b11101101, 0b00000101
    ])))
    stack = NegIntInfo().run(data, ignore_handler)
    assert len(stack) == 1
    stack2 = stack[0].run(data, handler.handler)
    assert len(stack2) == 0
    handler.assert_data('-3844467974')

    # NegInt length on 8 byte.
    data = CBORStream(BytesIO(bytes([
        0b00111011, 0b11100101, 0b00100101, 0b11101101, 0b00000101,
        0b11100101, 0b00100101, 0b11101101, 0b00000101
    ])))
    stack = NegIntInfo().run(data, ignore_handler)
    assert len(stack) == 1
    stack2 = stack[0].run(data, handler.handler)
    assert len(stack2) == 0
    handler.assert_data('-16511864218398878982')
