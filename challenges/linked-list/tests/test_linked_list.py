from linked_list import __version__
from linked_list.linked_list import LinkedList
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_linked_list():
    assert LinkedList()


def test_insert_node():
    list = LinkedList()
    list.insert('Tue')
    assert list.head.value == 'Tue'
    assert list.head.next == None
    

def test_insert_mult_nodes():
    list = LinkedList()
    list.insert('2020')
    list.insert('2019')
    list.insert('2018')
    assert list.head.value == '2018'
    assert list.head.next.value == '2019'
    

def test_if_data_in_list():
    list = LinkedList()
    list.insert('2020')
    list.insert('2019')
    list.insert('2018')
    assert list.includes('2020') == True
    assert list.includes('2021') == False


def test_all_values():
    list = LinkedList()
    list.insert('2020')
    list.insert('2019')
    list.insert('2018')
    assert str(list) == '2018 -> 2019 -> 2020 -> None'


def test_append():
    list = LinkedList(['2017', '2018'])
    list.append('2019')
    list.append('2020')
    assert (str(list).strip('[]')) == '2017 -> 2018 -> 2019 -> 2020 -> None'


def test_isert_before():
    list = list = LinkedList(['2017', '2018', '2020', '2021'])
    list.insert_before('2020', '2019')
    assert (str(list).strip('[]')) == '2017 -> 2018 -> 2019 -> 2020 -> 2021 -> None'


def test_insert_before_first():
    list = list = LinkedList(['2017', '2018', '2019'])
    list.insert_before('2017', '2016')
    assert (str(list).strip('[]')) == '2016 -> 2017 -> 2018 -> 2019 -> None'
    assert list.head.value == '2016'


def test_insert_after():
    list = LinkedList(['2017', '2019'])
    list.insert_after('2017', '2018')
    assert (str(list).strip('[]')) == '2017 -> 2018 -> 2019 -> None'


def test_insert_after_last():
    list = LinkedList(['2018', '2019'])
    list.insert_after('2019', '2020')
    assert (str(list).strip('[]')) == '2018 -> 2019 -> 2020 -> None'


def test_remove_node():
    list = LinkedList(['2018', '2019', '2020'])
    list.remove_node('2019')
    assert (str(list).strip('[]')) == '2018 -> 2020 -> None'


def test_remove_node_beginning():
    list = LinkedList(['2018', '2019'])
    list.remove_node('2018')
    assert (str(list).strip('[]')) == '2019 -> None'

def test_idx_out_of_range():
    with pytest.raises(Exception):
        list = LinkedList(['2018', '2019'])
        list.get_at_end_index(2)

def test_idx_and_len_list_same():
    list = LinkedList(['2018', '2019', '2020'])
    list.get_at_end_index(2)

def test_idx_negative():
    with pytest.raises(Exception):
        list = LinkedList(['2018', '2019', '2020'])
        list.get_at_end_index(-1)

def test_list_with_one_el():
    list = LinkedList(['2020'])
    list.get_at_end_index(0)

def test_middle_idx():
    list = LinkedList(['2016', '2017', '2018', '2020', '2021'])
    list.get_at_end_index(2)