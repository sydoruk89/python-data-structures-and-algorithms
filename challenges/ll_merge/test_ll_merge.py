import pytest
from ll_merge import Node, LinkedList, merge_list

def test_empty_lists():
    list_1 = LinkedList()
    list_2 = LinkedList()
    with pytest.raises(Exception):
        merge_list(list_1, list_2)

def test_merge():
    list_1 = LinkedList(['1', '3', '2'])
    list_2 = LinkedList(['5', '9', '4'])
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == '1 : 5 : 3 : 9 : 2 : 4 : None'

def test_1_shorter():
    list_1 = LinkedList(['1', '3'])
    list_2 = LinkedList(['5', '9', '4'])
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == '1 : 5 : 3 : 9 : 4 : None'

def test_2_shorter():
    list_1 = LinkedList(['1', '3', '2'])
    list_2 = LinkedList(['5', '9'])
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == '1 : 5 : 3 : 9 : 2 : None'

def test_1_list_1_element():
    list_1 = LinkedList([1])
    list_2 = LinkedList(['b', 'c'])
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == '1 : b : c : None'

def test_2_list_1_element():
    list_1 = LinkedList([1, 3])
    list_2 = LinkedList([2])
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == '1 : 2 : 3 : None'

def test_1_empty():
    list_1 = LinkedList()
    list_2 = LinkedList(['b', 'c'])
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == 'b : c : None'

def test_2_empty():
    list_1 = LinkedList(['a', 'b'])
    list_2 = LinkedList()
    list_3 = merge_list(list_1, list_2)
    assert list_3.__str__() == 'a : b : None'