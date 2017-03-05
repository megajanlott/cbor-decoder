import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from cbor import decode

if __name__ == '__main__':
    decoded = decode("Data to decode")

    print("Decoded:", decoded)
