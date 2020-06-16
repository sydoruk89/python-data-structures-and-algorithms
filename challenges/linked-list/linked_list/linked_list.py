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

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_

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

    def append(self, value):
        """
        Insert a new element at the end of the list.
        """
        node = Node(value)
        current = self.head
        if not self.head:
            self.head = node
            return
        while current.next_:
            current = current.next_
        current.next_ = node

    def insert_after(self, val, new_val):
        """
        Insert a new element after the given value
        """
        current = self.head
        if not current:
            raise Exception('List is empty')
        while current:
            if current.value == val:
                break
            current = current.next_
        if not current:
            raise Exception(f'Node with value {val} not found!')
        else:
            node = Node(new_val)
            node.next_ = current.next_
            current.next_ = node

    def get_at_end_index(k):
        """ 
        Return the node’s value that is k from the end of the linked list
        """
        current = self.head
        count = 0
        while current:
            if count == k:
                return current.value
            count += 1
            current = current.next

    def __str__(self):
        return f'Head: {self.head}'
 
    def __repr__(self):
        return f'{self.head}'
    

list = LinkedList()
a = list.append(1)
b = list.append(2)
c = list.append(3)
d = list.insert_after(2, 4)
print(list)
