from io import RawIOBase, BytesIO
from cbor.CBORStream import CBORStream
from cbor.HexBinStream import HexBinStream
from cbor.MajorType import MajorType
from cbor.Stack import Stack
from cbor.type.Array import ArrayInf, ArrayInfClose
from cbor.type.Map import MapInfValue, MapInfKey, MapInfClose
from cbor.type.TextString import TextStringInf
from cbor.type.ByteString import ByteStringInf


class Decoder:
    def close_inf(self, type, handler):
        if type == ArrayInf:
            ArrayInfClose(handler)
        elif (type == MapInfValue) or (type == MapInfKey):
            MapInfClose(handler)
        if type == TextStringInf:
            pass
        if type == ByteStringInf:
            pass

    def decode_array(self, array: bytes, handler):
        decode_stream = CBORStream(BytesIO(array))
        return self.__decode(decode_stream, handler)

    def decode_stream(self, stream: RawIOBase, handler):
        decode_stream = CBORStream(stream)
        return self.__decode(decode_stream, handler)

    def decode_hex_array(self, array: bytes, handler):
        decode_stream = HexBinStream(BytesIO(array))
        return self.__decode(decode_stream, handler)

    def decode_hex_stream(self, stream: RawIOBase, handler):
        decode_stream = HexBinStream(stream)
        return self.__decode(decode_stream, handler)

    def __decode(self, stream: CBORStream, handler):
        stack = Stack()
        stack.push(MajorType())

        while not stack.isEmpty():
            top = stack.pop()

            if type(top) == str and top == 'break':
                # should be ArrayInf, MapInfValue, MapInfKey
                # ByteStringInf, TextStringInf
                inf_type = stack.pop()
                self.close_inf(inf_type, handler)
            else:
                new_states = top.run(stream, handler)

                if new_states:
                    stack.push(new_states)
