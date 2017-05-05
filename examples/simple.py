import os
import sys
from io import RawIOBase, BytesIO
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from cbor.Decoder import Decoder


def printer(data):
    print(data, end='')


if __name__ == '__main__':
    d = Decoder()

    data = bytearray.fromhex('830182020363616263')

    print('')

    d.decode_array(data, printer)

    print('')

# A163617364A26161A0616263636465
# A163617364A26161A061628361786179A1617A63717171
# A26161830102636162636162A163666F6F83026461616161A163626172395B9F
# 830182020363616263
# A163617364A26161F46162836178FB 3FF3D70A3D70A3D7A1617A63717171
