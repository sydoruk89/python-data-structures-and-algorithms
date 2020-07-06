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


def merge_list(list_1, list_2):
    """
    Merge two linked lists and return a referense to the head of a new list.
    """

    current_1 = list_1.head
    current_2 = list_2.head

    if current_1 is None and current_2 is None:
        raise Exception("lists are empty")

    if not current_1:
        return list_2.head

    if not current_2:
        return list_1.head

    temp = current_2.next

    while current_1.next and current_2.next:
        current_1.next, current_2.next = current_2, current_1.next
        current_1 = current_2.next
        current_2, temp = temp, temp.next

    if not current_1.next:
        current_1.next = current_2
        return list_1.head

    if not current_2.next:
        current_1.next, current_2.next = current_2, current_1.next
        print(current_2, 'here')
        return list_1.head

list = LinkedList(['1', '3', '5'])
print(list)
list_1 = LinkedList(['2', '4', '6'])
print(merge_list(list, list_1))