# tests/test_stack.py

import pytest
from data_structures.stack import Stack

def test_stack_initialization():
    stack = Stack()
    assert len(stack) == 0
    assert stack.empty() is True

def test_push_to_stack():
    stack = Stack()
    stack.push(1)
    assert len(stack) == 1
    assert stack.top() == 1
    assert stack.empty() is False

def test_pop_from_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.top() == 1

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()

def test_top_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.top()

def test_stack_str_representation():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert str(stack) == '[1, 2]'

def test_stack_len():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
