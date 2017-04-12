import os
import sys
from cbor.Type7 import *
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from io import RawIOBase, BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream


def assertHandler(value):
    def handler(v):
        assert v == value
    return handler


def test_Type7Info():
    data = CBORStream(BytesIO(bytes([0b11111000])))
    assert type(Type7Info().run(data, None)) == Type7Read

    data = CBORStream(BytesIO(bytes([0b11111111])))
    assert Type7Info().run(data, None) == 'break'

    data = CBORStream(BytesIO(bytes([0b11111001])))
    result = Type7Info().run(data)
    assert type(result) == FloatRead
    assert result.bytes_to_read == 2


def test_Type7Read():
    data = CBORStream(BytesIO(bytes([0b11110100])))
    handler = assertHandler('pass')
    result = Type7Read().run(data, handler)
    assert result is None
