from cbor.Decoder import Decoder
from io import BytesIO
from tests.MockHandler import MockHandler
import json


def test_cbor():
    d = Decoder()
    handler = MockHandler()
    with open('tests/e2e/cases.json', encoding='utf8') as casesfile:
        cases = json.load(casesfile)
        for case in cases:
            if 'decoded' in case:
                # if 'gwGfAgP/ggQF' == case['cbor']:
                #     assert 0 == 1
                print(case)
                data = bytearray.fromhex(case['hex'])
                d.decode_array(data, handler.handler)
                expected = json.dumps(case['decoded'], separators=(',', ':'))
                handler.assert_data(expected)
