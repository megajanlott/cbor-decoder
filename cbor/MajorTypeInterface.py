from cbor.CBORStream import CBORStream


class MajorTypeInterface:
    def decode(self, stream: CBORStream):
        raise NotImplementedError
