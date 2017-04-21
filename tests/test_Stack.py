import pytest
from cbor.Stack import Stack


def test_init():
    stack = Stack()
    assert stack.items == []


def test_is_empty():
    stack = Stack()
    assert stack.isEmpty() is True
    stack = Stack()
    stack.push(10)
    assert stack.isEmpty() is False


def test_push():
    stack = Stack()
    stack.push(5)
    assert stack.items == [5]
    stack.push('test')
    assert stack.items == [5, 'test']


def test_push_array():
    stack = Stack()
    stack.push([3, 4])
    assert stack.items == [3, 4]
    stack.push(['test', [5, 6]])
    assert stack.items == [3, 4, 'test', [5, 6]]


def test_pop():
    stack = Stack()
    stack.push([1, 3, 4])
    assert stack.pop() == 4
    assert stack.items == [1, 3]
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_peek():
    stack = Stack()
    stack.push([1, 3, 4])
    assert stack.peek() == 4
    assert stack.items == [1, 3, 4]


def test_size():
    stack = Stack()
    stack.push(5)
    assert stack.size() == 1
    stack.push([6, 7])
    assert stack.size() == 3