import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from cbor.Stack import Stack


def test_init():
    stack = Stack()
    assert stack.items == []

<<<<<<< HEAD
def test_isEmpty():
    stack = Stack()
    assert stack.isEmpty() == True
    stack = Stack()
    stack.push(10)
    assert stack.isEmpty() == False
=======

def test_isEmpty():
    stack = Stack()
    assert stack.isEmpty() is True
    stack = Stack()
    stack.push(10)
    assert stack.isEmpty() is False

>>>>>>> adds E251 to ignored errors and makes tests pass the linter

def test_push():
    stack = Stack()
    stack.push(5)
    assert stack.items == [5]
    stack.push('test')
    assert stack.items == [5, 'test']

<<<<<<< HEAD
=======

>>>>>>> adds E251 to ignored errors and makes tests pass the linter
def test_push_array():
    stack = Stack()
    stack.push([3, 4])
    assert stack.items == [3, 4]
    stack.push(['test', [5, 6]])
    assert stack.items == [3, 4, 'test', [5, 6]]

<<<<<<< HEAD
=======

>>>>>>> adds E251 to ignored errors and makes tests pass the linter
def test_pop():
    stack = Stack()
    stack.push([1, 3, 4])
    assert stack.pop() == 4
    assert stack.items == [1, 3]
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()

<<<<<<< HEAD
=======

>>>>>>> adds E251 to ignored errors and makes tests pass the linter
def test_peek():
    stack = Stack()
    stack.push([1, 3, 4])
    assert stack.peek() == 4
    assert stack.items == [1, 3, 4]

<<<<<<< HEAD
=======

>>>>>>> adds E251 to ignored errors and makes tests pass the linter
def test_size():
    stack = Stack()
    stack.push(5)
    assert stack.size() == 1
    stack.push([6, 7])
    assert stack.size() == 3
