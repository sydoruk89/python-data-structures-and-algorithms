class Node:
    """
    This is the Node Class
    """

    def __init__(self, value):
        """
        This is my initialize of the Node
        """
        self.value = value
        self.next = None

    def __str__(self):
        """
        return string with the the object instance
        """
        return f'{self.value} : {self.next}'

    def __repr__(self):
        """
        return string with the the object instance
        """
        return self.value


class LinkedList:
    """
    This is my Class LinkedList with methods __init__ and __insert__
    """

    def __init__(self, nodes=None):
        """
        This is my initialize of LinkedList
        """
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next

    def __repr__(self):
        """
        Return an object instance
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        To traverse a linked list
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert(self, value):
        """ 
        Inserts a value in the beginning of the list
        """
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node
    def includes(self, data):
        """ 
        This func returns True if data is in linked list or False if it is not

        """
        current = self.head
        found = False
        while current and found is False:
            if current.value == data:
                found = True
            else:
                current = current.next
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
        while current.next:
            current = current.next
        current.next = node

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
            current = current.next
        if current:
            node = Node(new_val)
            node.next = current.next
            current.next = node
        else:
            raise Exception(f'Node with value {val} not found!')

    def insert_before(self, val, new_val):
        """ 
        Insert a new element before the given value
        """
        prev = self.head
        new_node = Node(new_val)
        if not self.head:
            raise Exception("List is empty")

        if prev.value == val:
            return self.insert(new_val)

        for node in self:
            if node.value == val:
                prev.next = new_node
                new_node.next = node
                return
            prev = node

        raise Exception(f'Node with value {val} not found!')

    def remove_node(self, val):
        if not self.head:
            raise Exception("List is empty")

        if self.head.value == val:
            self.head = self.head.next
            return

        prev = self.head
        for node in self:
            if node.value == val:
                prev.next = node.next
                return
        prev = node

        raise Exception(f'Node with value {val} not found')

    def get_at_end_index(self, n):
        prev = None
        current = self.head
        follow = current.next
        while current:
            current.next = prev
            prev = current
            current = follow
            if follow:
                follow = follow.next
        self.head = prev

        count = 0
        for el in self:
            if count == n:
                return el.value
            count += 1
        raise Exception(f'Node at index {n} is out of range!')
