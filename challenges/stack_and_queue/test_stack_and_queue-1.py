from stacks_and_queues import Node, Stack, Queue
import pytest


def test_push_stack():
    stack = Stack()
    stack.push('1')
    assert stack.top.value == '1'
    assert stack.top.next == None

def test_mult_push():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    assert stack.__str__() == '2 -> 1 -> None'

def test_pop_stack():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    assert stack.pop() == '2'

def test_mult_pop_stack():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True

def test_peek_stack():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    assert stack.peek() == '2'

def test_inst_empty_stack():
    stack = Stack()
    assert stack.top == None

def test_exceptions_():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()
        stack.peek()
    
def test_enqueue():
    pass
    