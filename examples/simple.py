import os
import sys
from io import RawIOBase, BytesIO
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from cbor.Decoder import Decoder


def printer(data):
    print("Received:", data)


if __name__ == '__main__':
    d = Decoder()
    data = bytes(3)
    print(BytesIO(data))
    print("Decoded:", d.decode_array(data, printer))
