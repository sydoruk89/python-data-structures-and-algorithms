class Node_q:
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

        if self.front is None:
            return True
        return False

    def enqueue(self, val):
        """Method that adds an element to the end of the queue"""

        if self.is_empty():
            self.front = self.rear = Node_q(val)
        else:
            new_node = Node(val)
            self.rear.next, self.rear = new_node, new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns its value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            raise Exception('Queue is empty!')

    def peek(self):
        """Method returns the value of the front node"""

        if not self.is_empty():
            return self.front.value
        return None


class Node:
    """
    Node class which instantiates node value with right or left direction

    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    BinaryTree class instantiation with pre_order, in_order and post_order methods.
    """
    def __init__(self, root):
        self.root = Node(root)

    def pre_order(self):
        """
         Traverse through binary tree in next order: root >> left >> right
        """
        otput = []

        def traverse(node):
            if not node:
                return
            otput.append(node.value)

            traverse(node.left)

            traverse(node.right)

        traverse(self.root)

        return otput
    
    def in_order(self):
        """
         Traverse through binary tree in next order: left >> root >> right
        """
        otput = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)

            otput.append(node.value)

            traverse(node.right)

        traverse(self.root)

        return otput

    def post_order(self):
        """
         Traverse through binary tree in next order: left >> right >> root
        """
        otput = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)

            traverse(node.right)

            otput.append(node.value)

        traverse(self.root)

        return otput

    def find_maximum_value(self):
        """
        This method returns the max value of the BST
        """
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    def breadth_first(self):
        """
        This method returns a list of the values in the tree in the order they were encountered
        """
        breadth = Queue()
        breadth.enqueue(self.root)
        output = []
        while breadth.peek():
            output.append(breadth.peek())
            node = breadth.dequeue()
            if node.left:
                breadth.enqueue(node.left)
            if node.right:
                breadth.enqueue(node.right)
        return output
 

class BST(BinaryTree):
    """
    Binary search tree class with 'add' and 'contains' methods.
    """
    def add(self, value):
        """
        Method adds value to the left if smaller then root or to the right if grater.

        """
        def traverse(node, node_to_add):
            if not node:
                return

            if node_to_add.value < node.value:
                if not node.left:
                    node.left = node_to_add
                else:
                    traverse(node.left, node_to_add)
            else:
                if not node.right:
                    node.right = node_to_add
                else:
                    traverse(node.right, node_to_add)

        n = Node(value)
        if not self.root:
            self.root = n
            return
        
        traverse(self.root, n)

    def contains(self, key):
        """
        This method accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once
        """
        def traverse(node, key):
            if not node:
                print('is not found')
            if node.value == key:
                print('found')
            elif node.value > key:
                if not node.left:
                    print('is not found')
                else:
                    traverse(node.left, key)
            else:
                if not node.right:
                    print('is not found')
                else:
                    traverse(node.right, key)

        traverse(self.root, key)

        
bst = BST(7)
bst.add(4)
bst.add(3)
bst.add(2)
bst.add(5)
bst.add(9)
bst.add(11)
print(bst.breadth_first())
