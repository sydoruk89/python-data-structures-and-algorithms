class Node:
    """Creates a nodes for the tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Creates a binary tree"""
    def __init__(self):
        self.root = None


def fizz_buzz(value):
    """Function return Fizz, Buzz or FizzBuzz"""
    if not value % 15:
        return "FizzBuzz"
    if not value % 5:
        return "Buzz"
    if not value % 3:
        return "Fizz"
    else:
        return str(value)

def fizz_buzz_tree(tree):
    """Changes values from the given tree in appliance with fizz_buzz func """

    new_tree = BinaryTree()

    if not tree.root:
        return new_tree

    def recursive(current):
        """Func to go recursively through each element in given tree and return a new tree"""
        node = Node(fizz_buzz(current.value))

        if current.left:
            node.left = recursive(current.left)
        if current.right:
            node.right = recursive(current.right)
        return node

    new_tree.root = recursive(tree.root)
    return new_tree
