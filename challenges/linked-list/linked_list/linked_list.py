class Node:
    """
    This is the Node Class
    """

    def __init__(self, value, next_=None):
        """
        This is my initialize of the Node
        """
        self.value = value
        self.next_ = next_

    def get_data(self):
        """
        Func() returns current value
        """
        return self.value

    def get_next(self):
        """
        Func() returns next value 
        """
        return self.next_

    def __str__(self):
        """
        return string with the the object instance
        """
        return f'{self.value} : {self.next_}'

    def __repr__(self):
        """
        return string with the the object instance
        """
        return (self.value, self.next_)


class LinkedList:
    """
    This is my Class LinkedList with methods __init__ and __insert__
    """

    def __init__(self):
        """
        This is my initialize of LinkedList
        """
        self.head = None

    def insert(self, value):
        """ 
        Inserts a value in the beginning of the list
        """
        node = Node(value)
        if self.head is not None:
            node.next_ = self.head
        self.head = node

    def includes(self, data):
        """ 
        This func returns True if data is in linked list or False if it is not

        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def __str__(self):
        return f'Head: {self.head}'
 
    def __repr__(self):
        return f'{self.head}'


list = LinkedList()

