from quick_sort import quickSort
import pytest

def test_random_list():
    test_list = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    quickSort(test_list, 0, len(test_list)-1)
    assert test_list == expected

def test_few_uniques():
    test_list = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    quickSort(test_list, 0, len(test_list)-1)
    assert test_list == expected

def test_nearly_sorted():
    test_list = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    quickSort(test_list, 0, len(test_list)-1)
    assert test_list == expected

def test_couple_zeros():
    test_list = [0,0,1,1,0]
    expected = [0,0,0,1,1]
    quickSort(test_list, 0, len(test_list)-1)
    assert test_list == expected