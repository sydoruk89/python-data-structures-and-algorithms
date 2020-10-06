class Node:
    """
    Node class initilizing
    """
    def __init__(self, value, next=None):
        """
        Init node instance with value and next element
        """
        self.value = value
        self.next = next

    def __str__(self):
        """ Return an object instance
        """
        return f'{self.value} -> {self.next}'

    def __repr__(self):
        """
        Return an object instance
        """
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
    """class Queue"""

    def __init__(self, next=None):
        """Initiate class"""

        self.front = None
        self.rear = None

    def __str__(self) -> str:
        """Informal string representation
        """
        output = []
        curr = self.front
        while curr is not None:
            output.append(curr.value)
            curr = curr.next
        return " -> ".join(output)
    

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, val):
        """Method that adds an element to the end of the queue"""

        if self.is_empty():
            self.front = self.rear = Node(val)
        else:
            new_node = Node(val)
            self.rear.next, self.rear = new_node, new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns its value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            raise Exception('Queue is empty!')

    def peek(self):
        """Method returns the value of the front node"""

        if not self.is_empty():
            return self.front.value
        return None