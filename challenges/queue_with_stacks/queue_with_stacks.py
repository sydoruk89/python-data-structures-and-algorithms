class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'{self.value} -> {self.next}'

    def __repr__(self):
        return f'{self.value}'


class Stack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        return f'{self.top}'

    def __repr__(self):
        return f'{self.top}'

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            stored_top = self.top
            self.top = self.top.next
            stored_top.next = None
            return stored_top.value
        else:
            raise Exception('Stack is empty')
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise Exception('There is no top!')

class PseudoQueue:
    """
    Queue with 2 stacks
    """
    def __init__(self, stack):
        self.stack = stack
        self.stack_2 = Stack()

    def enqueue(self, value):
        """
        Inserts a value into the PseudoQueue
        """
        self.stack.push(value)
        return self.stack.top.value

    def dequeue(self):
        """
        Extracts a value from the PseudoQueue
        """
        if self.stack.top == None:
            raise Exception('PseudoQueue is empty')
        while self.stack.peek():
            self.stack_2.push(self.stack.pop())
            return self.stack_2.pop()