# API

## Installation

You can install `cbor-decoder` from PyPI:

```
$ pip install cbor-decoder
```

## Example

``` python
from cbor.Decoder import Decoder

def printer(data):
    print('Received:', data)


if __name__ == '__main__':
    decoder = Decoder()

    data = bytearray.fromhex('830182020339 01C7')

    decoder.decode_array(data, printer)

    # prints: [1,[2,3],-456]
```

## Methods

### `d = Decoder()`

Creates a new `cbor.Decoder` instance.

### `d.decode_array(data: bytes, handler)`

Decodes `data` which is a binary byte array of CBOR data to encode. The decoded values will be passed to the `handler` callback in chunks of data.

### `d.decode_stream(stream: RawIOBase, handler)`

Decodes `data` which is a binary stream of CBOR data to encode. The decoded values will be passed to the `handler` callback in chunks of data.

### `d.decode_hex_array(data: bytes, handler)`

Decodes `data` which is a hexadecimal array of CBOR data to encode. The decoded values will be passed to the `handler` callback in chunks of data.

### `d.decode_hex_stream(stream: RawIOBase, handler)`

Decodes `data` which is a hexadecimal stream of CBOR data to encode. The decoded values will be passed to the `handler` callback in chunks of data.
