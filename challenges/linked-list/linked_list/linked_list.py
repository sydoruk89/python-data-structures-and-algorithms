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

    def __str__(self):
        return f'{self.value} : {self.next_}'

    def __repr__(self):
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

    def __str__(self):
        return f'Head: {self.head}'
 
    def __repr__(self):
        return f'{self.head}'


list = LinkedList()
list.insert('2020')
list.insert('2019')
list.insert('2018')

print(list.includes('2089'))
