import os
import sys
from cbor.Type7 import *
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from io import RawIOBase, BytesIO
from cbor.MajorType import MajorType
from cbor.CBORStream import CBORStream


def test_Type7Info():
    data = CBORStream(BytesIO(bytes([0b11111000])))
    assert Type7Info().run(data, None) == Type7Read
    data = CBORStream(BytesIO(bytes([0b11111111])))
    assert Type7Info().run(data, None) == 'break'
    data = CBORStream(BytesIO(bytes([0b11111001])))
    assert Type7Info().run(data, None) == FloatRead(2)

def test_Type7Read():
    data = CBORStream(BytesIO(bytes([0b11110100])))
    assert Type7Read().run(data, None) == None