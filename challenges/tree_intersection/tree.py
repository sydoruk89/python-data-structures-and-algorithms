class Node:
    """
    Node class which instantiates node value with right or left direction

    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


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
            return temp
        else:
            raise Exception('Queue is empty!')

    def peek(self):
        """Method returns the value of the front node"""

        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    """
    BinaryTree class instantiation with pre_order, in_order and post_order methods.
    """
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "pre_order":
            return self.pre_order(self.root, "")
        elif traversal_type == "in_order":
            return self.in_order(self.root, "")
        elif traversal_type == "post_order":
            return self.post_order(self.root, "")
        elif traversal_type == "breadth_first":
            return self.breadth_first()
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def pre_order(self, start, traversal):
        """
         Traverse through binary tree in next order: root >> left >> right
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal
    
    def in_order(self, start, traversal):
        """
         Traverse through binary tree in next order: left >> root >> right
        """
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        """
         Traverse through binary tree in next order: left >> right >> root
        """
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def find_maximum_value(self):
        """
        This method returns the max value of the BST
        """
        q = Queue()
       
        if not self.root:
            return None

        max_val = self.root.value
        q.enqueue(self.root)

        while not q.is_empty():
            node_front = q.dequeue().value
            if node_front.value > max_val:
                max_val = node_front.value

            if node_front.left:
                q.enqueue(node_front.left)
            if node_front.right:
                q.enqueue(node_front.right)

        return max_val
    
    def breadth_first(self):
        """
        This method returns a list of the values in the tree in the order they were encountered
        """
        if not self.root:
            return None

        q = Queue()
        q.enqueue(self.root)
        nodes = ''
        while not q.is_empty():
            node_front = q.dequeue().value
            nodes += str(node_front.value) + "-"
            if node_front.left:
                q.enqueue(node_front.left)
            if node_front.right:
                q.enqueue(node_front.right)
        return nodes
 

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


