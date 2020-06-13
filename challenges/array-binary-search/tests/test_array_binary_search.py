from array_binary_search import __version__
from array_binary_search.array_binary_search import BinarySearch


def test_version():
    assert __version__ == '0.1.0'


def test_passed():
    actual = BinarySearch([1, 2, 3, 4, 5], 4)
    expected = 3
    assert actual == expected

def test_neg_passed():
    actual = BinarySearch([-4, -3, -2, -1, 0], -3)
    expected = 1
    assert actual == expected

def test_failed():
    actual = BinarySearch([1, 3, 5, 7, 9], 3)
    expected = 2
    assert actual != expected 

def test_random_failed():
    actual = BinarySearch([1, 7, 3, 8, 5], 5)
    expected = 4
    assert actual != expected