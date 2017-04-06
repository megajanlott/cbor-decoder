from cbor.CBORStream import CBORStream
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def run(self, stream: CBORStream, handler):
        raise NotImplementedError
