from merge_sort import merge_sort
import pytest

def test_random_list():
    my_list = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    merge_sort(my_list)
    actual = my_list
    assert actual == expected

def test_few_uniques():
    my_list = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    merge_sort(my_list)
    actual = my_list
    assert actual == expected

def test_nearly_sorted():
    my_list = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    merge_sort(my_list)
    actual = my_list
    assert actual == expected

def test_couple_zeros():
    my_list = [0,0,1,1,0]
    expected = [0,0,0,1,1]
    merge_sort(my_list)
    actual = my_list
    assert actual == expected