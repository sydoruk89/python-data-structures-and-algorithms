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

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.rear = None

    def __str__(self):
        return f'{self.rear}'
    
    def enqueue(self, value):
        prev = self.rear
        new_node = Node(value)

    def dequeue(self):
        if self.front:
            temp = self.front
            front = self.front.next
            temp.next = None
            return temp.value
        else:
            raise Exception('Queue is empty')

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise Exception('There is no front!')

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

q = Queue()
q.enqueue('1')
print(q)