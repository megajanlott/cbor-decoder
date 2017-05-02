class MockHandler:

    def __init__(self):
        self.data = ''

    def handler(self, value):
        self.data += value

    def assert_data(self, data):
        assert self.data == data
        self.data = ''
