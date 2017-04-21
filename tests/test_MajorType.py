from io import BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream
from cbor.type.UInt import UIntInfo
from cbor.type.Neg_Int import NegIntInfo


def test_run_uint():
    mt = MajorType()
    data = CBORStream(BytesIO(bytes([0b00010101])))
    assert type(mt.run(data, None)) is UIntInfo
    data = CBORStream(BytesIO(bytes([0b00000000])))
    assert type(mt.run(data, None)) is UIntInfo
    data = CBORStream(BytesIO(bytes([0b00010111])))
    assert type(mt.run(data, None)) is UIntInfo
    data = CBORStream(BytesIO(bytes([0b00011111])))
    assert type(mt.run(data, None)) is UIntInfo


def test_run_int():
    mt = MajorType()
    data = CBORStream(BytesIO(bytes([0b00110101])))
    assert type(mt.run(data, None)) is NegIntInfo
    data = CBORStream(BytesIO(bytes([0b00100000])))
    assert type(mt.run(data, None)) is NegIntInfo
    data = CBORStream(BytesIO(bytes([0b00110111])))
    assert type(mt.run(data, None)) is NegIntInfo
    data = CBORStream(BytesIO(bytes([0b00111111])))
    assert type(mt.run(data, None)) is NegIntInfo
