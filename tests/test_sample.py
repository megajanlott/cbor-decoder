import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from cbor import decode


def test():
    assert decode("anything") == "Decoded data"
