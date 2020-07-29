import pytest
from tree import BinaryTree, BST, Node


def test_tree_with_single_node():
    tree = BinaryTree(1)
    assert tree != None


def test_pre_order():
    tree = BST(3)
    tree.add(1)
    tree.add(4)
    actual = tree.print_tree("pre_order")
    expected = '3-1-4-'
    assert actual == expected


def test_in_order():
    tree = BST(7)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    tree.add(5)
    tree.add(9)
    tree.add(10)
    assert tree.print_tree('in_order') == '2-3-4-5-7-9-10-'


def test_post_order():
    tree = BST(7)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    tree.add(5)
    tree.add(9)
    tree.add(10)
    assert tree.print_tree('post_order') == '2-3-5-4-10-9-7-'


def test_max_val_one_el():
    tree = BinaryTree(7)
    assert tree.find_maximum_value() == 7


def test_max_val():
    tree = BinaryTree(2)
    tree.root = Node(-1)
    tree.root.left = Node(4)
    tree.root.left.left = Node(7)
    tree.root.left.left.left = Node(3)
    tree.root.left.left.left.left = Node(8)
    assert tree.find_maximum_value() == 8


def test_max_val_same_el():
    tree = BinaryTree(1)
    tree.root.left = Node(-3)
    tree.root.left.left = Node(-3)
    tree.root.left.left.left = Node(-3)
    tree.root.left.left.left.left = Node(-3)
    assert tree.find_maximum_value() == 1


def test_breadth_first_bt():
    tree = BinaryTree(4)
    tree.root.left = Node(5)
    tree.root.right = Node(7)
    tree.root.left.left = Node(9)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(8)
    assert tree.print_tree('breadth_first') == '4-5-7-9-3-8-'


def test_breadth_first_left():
    tree = BinaryTree(2)
    tree.root.left = Node(1)
    tree.root.left.left = Node(1)
    tree.root.left.left.left = Node(1)
    assert tree.print_tree('breadth_first') == '2-1-1-1-'


def test_breadth_first_bst():
    tree = BST(7)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    tree.add(5)
    tree.add(9)
    tree.add(10)
    assert tree.print_tree('breadth_first') == '7-4-9-3-5-10-2-'
