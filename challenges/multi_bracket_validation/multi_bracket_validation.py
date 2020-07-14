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


def multi_bracket_validation(input):
    stack = Stack()
    if not input:
        return False
    for i in input:
        if i == '(':
            stack.push(')')
        elif i == '{':
            stack.push('}')
        elif i == '[':
            stack.push(']')
        elif i == ')' or i == '}' or i == ']':
            if stack.is_empty() or stack.pop() != i:
                return False
    return stack.is_empty()

print(multi_bracket_validation('n'))