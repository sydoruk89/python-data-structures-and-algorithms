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
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    assert q.__str__() == '1 -> 2'
    
def test_is_empty():
    q = Queue()
    assert q.is_empty() == True

def test_peek():
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    assert q.peek() == '1'

def test_dequeue():
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    assert q.dequeue().__str__() == '1 -> None'
    assert q.dequeue().__str__() == '2 -> None'

def test_dequeue_empty():
    q = Queue()
    with pytest.raises(Exception):
        q.dequeue()
