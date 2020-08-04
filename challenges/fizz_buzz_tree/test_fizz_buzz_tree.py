from fizz_buzz_tree import Node, BinaryTree, fizz_buzz, fizz_buzz_tree

import pytest

@pytest.fixture
def test_tree():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(1)
    tree.root.right = Node(15)
    tree.root.left.left = Node(21)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(20)
    tree.root.left.left.left = Node(6)
    tree.root.right.right.left = Node(10)
    return tree

def test_empty_tree():
    tree = BinaryTree()
    new_tree = fizz_buzz_tree(tree)
    assert new_tree.root == None

def test_fizz_buzz(test_tree):
    new_tree = fizz_buzz_tree(test_tree)
    assert new_tree.root.value == "Buzz"

def test_no_fizz_buzz(test_tree):
    new_tree = fizz_buzz_tree(test_tree)
    assert new_tree.root.left.value == "1"

def test_fizz_buzz_15(test_tree):
    new_tree = fizz_buzz_tree(test_tree)
    assert new_tree.root.right.value == "FizzBuzz"

def test_fizz_buzz21(test_tree):
    new_tree = fizz_buzz_tree(test_tree)
    assert new_tree.root.left.left.value == "Fizz"

def test_fizz_buzz10(test_tree):
    new_tree = fizz_buzz_tree(test_tree)
    assert new_tree.root.right.right.left .value == "Buzz"