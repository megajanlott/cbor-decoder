from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.Array import ArrayInfo, ArrayRead, ArrayLen
from tests.MockHandler import MockHandler


def ignore_handler(v):
    return


def test_run_array_probe():
    data = CBORStream(BytesIO(bytes([0b10000001])))
    assert type(MajorType().run(data, None)) == ArrayInfo


def test_run_array_length():
    # Array length lower than 24.
    data = CBORStream(BytesIO(bytes([0b10000011])))
    stack = ArrayInfo().run(data, ignore_handler)
    assert len(stack) == 2
    assert type(stack[0]) == ArrayRead
    assert stack[0] == ArrayRead(3)
    assert type(stack[1]) == MajorType


def test_run_array_length_multibyte():
    # Array length on 1 byte.
    data = CBORStream(BytesIO(bytes([
        0b10011000, 0b1
    ])))
    stack = ArrayInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == ArrayLen
    assert stack[0] == ArrayLen(1)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 2
    assert type(stack2[0]) == ArrayRead
    assert stack2[0] == ArrayRead(1)
    assert type(stack2[1]) == MajorType

    # Array length on 2 bytes.
    data = CBORStream(BytesIO(bytes([
        0b10011001, 0b1, 0b0
    ])))
    stack = ArrayInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == ArrayLen
    assert stack[0] == ArrayLen(2)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 2
    assert type(stack2[0]) == ArrayRead
    assert stack2[0] == ArrayRead(1 << 8)
    assert type(stack2[1]) == MajorType

    # Array length on 4 bytes.
    data = CBORStream(BytesIO(bytes([
        0b10011010, 0b1, 0b0, 0b0, 0b0
    ])))
    stack = ArrayInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == ArrayLen
    assert stack[0] == ArrayLen(4)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 2
    assert type(stack2[0]) == ArrayRead
    assert stack2[0] == ArrayRead(1 << 24)
    assert type(stack2[1]) == MajorType

    # Array length on 8 bytes.
    data = CBORStream(BytesIO(bytes([
        0b10011011, 0b1, 0b0, 0b0, 0b0, 0b0, 0b0, 0b0, 0b0
    ])))
    stack = ArrayInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == ArrayLen
    assert stack[0] == ArrayLen(8)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 2
    assert type(stack2[0]) == ArrayRead
    assert stack2[0] == ArrayRead(1 << 56)
    assert type(stack2[1]) == MajorType


def test_run_array_read():
    handler = MockHandler()

    # Empty array.
    data = CBORStream(BytesIO(bytes([0b10000000])))
    stack = ArrayInfo().run(data, handler.handler)
    assert len(stack) == 0
    handler.assert_data('[]')
