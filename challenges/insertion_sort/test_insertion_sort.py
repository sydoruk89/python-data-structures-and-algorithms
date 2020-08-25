from insertion_sort import selection_sort
import pytest

def test_random_list():
    expected = [4, 8, 15, 16, 23, 42]
    actual = selection_sort([8,4,23,42,16,15])
    assert actual == expected

def test_few_uniques():
    expected = [5,5,5,7,7,12]
    actual = selection_sort([5,12,7,5,5,7])
    assert actual == expected

def test_nearly_sorted():
    expected = [2,3,5,7,11,13]
    actual = selection_sort([2,3,5,7,13,11])
    assert actual == expected

def test_couple_zeros():
    expected = [0,0,0,1,1]
    actual = selection_sort([0,0,1,1,0])
    assert actual == expected
