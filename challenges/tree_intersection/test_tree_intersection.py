import pytest
from tree_intersection import tree_intersection
from tree import BinaryTree, Node

@pytest.fixture()
def tree1():
    bt1 = BinaryTree(1)
    bt1.root.left = Node(2)
    bt1.root.right = Node(3)
    bt1.root.left.left = Node(4)
    bt1.root.right.right = Node(5)

    return bt1

@pytest.fixture()
def tree2():
    bt2 = BinaryTree(1)
    bt2.root.left = Node(3)
    bt2.root.right = Node(4)
    bt2.root.left.left = Node(4)
    bt2.root.right.right = Node(5)

    return bt2


def test_tree_intersection(tree1, tree2):
        expected = set((1, 4, 5))
        actual = tree_intersection(tree1, tree2)
        assert actual == expected


def test_one_tree_is_empty(tree1):
    tree2 = BinaryTree()
    expected = set()
    actual = tree_intersection(tree1, tree2)
    assert actual == expected

def test_both_empty():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    assert tree_intersection(tree1, tree2) == {None}

def test_differ_trees(tree1):
    bt2 = BinaryTree(6)
    bt2.root.left = Node(7)
    bt2.root.right = Node(8)
    bt2.root.left.left = Node(9)
    bt2.root.right.right = Node(10)
    expected = set()
    actual = tree_intersection(tree1, bt2)
    assert actual == expected
