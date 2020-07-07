from queue_with_stacks import Node, Stack, PseudoQueue
import pytest

@pytest.fixture
def init_stack():
    new_stack = Stack()
    my_list = [1, 2, 3, 4]
    for el in my_list:
       new_stack.push(el)

    return new_stack

def test_stack_exist(init_stack):
    q = PseudoQueue(init_stack)
    assert q.stack.peek() == 4

def test_enqueue(init_stack):
    q = PseudoQueue(init_stack)
    q.enqueue(5)
    assert q.stack.peek() == 5

def test_dequeue(init_stack):
    q = PseudoQueue(init_stack)
    assert q.dequeue() == 4

def test_dequeue_empty():
    q = PseudoQueue(Stack())
    with pytest.raises(Exception):  
        val = pseudo_q.dequeue()