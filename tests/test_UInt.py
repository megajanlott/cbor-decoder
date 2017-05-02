from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.UInt import UIntInfo


def ignore_handler(v):
    return


def test_run_uint_probe():
    data = CBORStream(BytesIO(bytes([0b00000001])))
    assert type(MajorType().run(data, None)) == UIntInfo


def test_run_uint_same_byte():
    # UInt length lower than 24.
    data = CBORStream(BytesIO(bytes([0b00010111])))
    stack = UIntInfo().run(data, ignore_handler)
    assert stack == 23


def test_run_uint_multibyte():
    # UInt length on 1 byte.
    data = CBORStream(BytesIO(bytes([
        0b00011000, 0b11100101
    ])))
    stack = UIntInfo().run(data, ignore_handler)
    assert stack == 229

    # UInt length on 2 byte.
    data = CBORStream(BytesIO(bytes([
        0b00011001, 0b11100101, 0b10101010
    ])))
    stack = UIntInfo().run(data, ignore_handler)
    assert stack == 58794

    # UInt length on 4 byte.
    data = CBORStream(BytesIO(bytes([
        0b00011010, 0b11100101, 0b00100101, 0b11101101, 0b00000101
    ])))
    stack = UIntInfo().run(data, ignore_handler)
    assert stack == 3844467973

    # UInt length on 8 byte.
    data = CBORStream(BytesIO(bytes([
        0b00011011, 0b11100101, 0b00100101, 0b11101101, 0b00000101, 0b11100101, 0b00100101, 0b11101101, 0b00000101
    ])))
    stack = UIntInfo().run(data, ignore_handler)
    assert stack == 16511864218398878981