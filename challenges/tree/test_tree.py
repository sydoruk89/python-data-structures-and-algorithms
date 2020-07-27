import pytest
from tree import BinaryTree, BST


def test_instantiate_empty_tree():
    actual = BinaryTree()
    expected = None
    assert actual != expected


def test_tree_with_single_node():
    bst = BST()
    bst.add(1)
    actual = bst.pre_order()
    expected = [1]
    assert actual == expected


def test_left_right_child():
    bst = BST()
    bst.add(3)
    bst.add(1)
    bst.add(4)
    actual = bst.pre_order()
    expected = [3, 1, 4]
    assert actual == expected


def test_pre_order():
    bst = BST()
    bst.add(7)
    bst.add(4)
    bst.add(3)
    bst.add(2)
    bst.add(5)
    bst.add(9)
    bst.add(10)
    assert bst.pre_order() == [7, 4, 3, 2, 5, 9, 10]


def test_in_order():
    bst = BST()
    bst.add(7)
    bst.add(4)
    bst.add(3)
    bst.add(2)
    bst.add(5)
    bst.add(9)
    bst.add(10)
    assert bst.in_order() == [2, 3, 4, 5, 7, 9, 10]


def test_post_order():
    bst = BST()
    bst.add(7)
    bst.add(4)
    bst.add(3)
    bst.add(2)
    bst.add(5)
    bst.add(9)
    bst.add(10)
    assert bst.post_order() == [2, 3, 5, 4, 10, 9, 7]
