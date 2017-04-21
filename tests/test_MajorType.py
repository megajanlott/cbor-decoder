# from io import BytesIO
# from cbor.MajorType import MajorType
# from cbor.CBORStream import CBORStream
#
#
# def test_run_uint():
#     mt = MajorType()
#     data = CBORStream(BytesIO(bytes([0b00010101])))
#     assert mt.run(data, None) is None
#     data = CBORStream(BytesIO(bytes([0b00000000])))
#     assert mt.run(data, None) is None
#     data = CBORStream(BytesIO(bytes([0b00010111])))
#     assert mt.run(data, None) is None
#     data = CBORStream(BytesIO(bytes([0b00011111])))
#     assert mt.run(data, None) is None
#
#
# def test_run_int():
#     mt = MajorType()
#     data = CBORStream(BytesIO(bytes([0b00110101])))
#     assert mt.run(data, None) is None
#     data = CBORStream(BytesIO(bytes([0b00100000])))
#     assert mt.run(data, None) is None
#     data = CBORStream(BytesIO(bytes([0b00110111])))
#     assert mt.run(data, None) is None
#     data = CBORStream(BytesIO(bytes([0b00111111])))
#     assert mt.run(data, None) is None