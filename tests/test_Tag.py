from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.Tag import TagInfo, TagRead
from tests.MockHandler import MockHandler


def ignore_handler(v):
    return


def test_run_tag_probe():
    data = CBORStream(BytesIO(bytes([0b11000001])))
    assert type(MajorType().run(data, None)) == TagInfo


def test_run_tag_length():
    # Tag length lower than 24.
    data = CBORStream(BytesIO(bytes([0b11000011])))
    stack = TagInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == MajorType


def test_run_tag_length_multibyte():
    # Tag length on 1 byte.
    data = CBORStream(BytesIO(bytes([
        0b11011000, 0b1
    ])))
    stack = TagInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == TagRead
    assert stack[0] == TagRead(1)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 1
    assert type(stack2[0]) == MajorType

    # Tag length on 2 bytes.
    data = CBORStream(BytesIO(bytes([
        0b10011001, 0b1, 0b0
    ])))
    stack = TagInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == TagRead
    assert stack[0] == TagRead(2)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 1
    assert type(stack2[0]) == MajorType

    # Tag length on 4 bytes.
    data = CBORStream(BytesIO(bytes([
        0b10011010, 0b1, 0b0, 0b0, 0b0
    ])))
    stack = TagInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == TagRead
    assert stack[0] == TagRead(4)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 1
    assert type(stack2[0]) == MajorType

    # Tag length on 8 bytes.
    data = CBORStream(BytesIO(bytes([
        0b10011011, 0b1, 0b0, 0b0, 0b0, 0b0, 0b0, 0b0, 0b0
    ])))
    stack = TagInfo().run(data, ignore_handler)
    assert len(stack) == 1
    assert type(stack[0]) == TagRead
    assert stack[0] == TagRead(8)
    stack2 = stack[0].run(data, ignore_handler)
    assert len(stack2) == 1
    assert type(stack2[0]) == MajorType


def test_run_tag_read():
    handler = MockHandler()

    # No output expected.
    data = CBORStream(BytesIO(bytes([0b11000000])))
    stack = TagInfo().run(data, handler.handler)
    assert len(stack) == 1
    assert type(stack[0]) == MajorType
    handler.assert_data('')
