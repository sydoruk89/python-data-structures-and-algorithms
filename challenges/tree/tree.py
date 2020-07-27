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
    def __init__(self):
        self.root = None

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
        

bst = BST()
bst.add(7)
bst.add(4)
bst.add(3)
bst.add(2)
bst.add(5)
bst.add(9)
bst.add(10)
print(bst.contains(33))
