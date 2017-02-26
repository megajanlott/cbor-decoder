# cbor-decoder

`cbor-decoder` is a Python library for decoding raw **CBOR** data to JSON or
Python data structures.

## roadmap

1. get familiar with CBOR
  - study the [standard](https://tools.ietf.org/html/rfc7049), especially
    **Section 2 and 3**.
  - try it out: [cbor.me](http://cbor.me/)
  - [other implementations](http://cbor.io/impls.html)
2. create development environment
  - set up repository structure
  - set up `pip install` mechanism
  - set up testing environment with [`pytest`](http://docs.pytest.org/en/latest/)
  - set up continuous integration with [`travis`](https://travis-ci.com/)
3. implementation
  - possible sequence
    1. create a simple interface
    2. start with the *major types*
      - every type is a separated task
      - more complex ones can be split
    3. add indefinite length support
    4. add floating-point numbers and values with no content
    5. create different interfaces
    6. tag and support for other things if there is time
  - every feature developed on **separate branch**
    - with **tests** and **documentation**
    - with coverage report
    - merged into master after review and if CI is passing
  - release
4. create a simple sample application if there is time
