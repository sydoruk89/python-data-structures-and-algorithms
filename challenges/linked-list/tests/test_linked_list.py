from linked_list import __version__
from linked_list.linked_list import LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_linked_list():
    assert LinkedList()


def test_insert_node():
    list = LinkedList()
    list.insert('Tue')
    assert list.head.value == 'Tue'
    assert list.head.next_ == None
    

def test_insert_mult_nodes():
    list = LinkedList()
    list.insert('2020')
    list.insert('2019')
    list.insert('2018')
    assert list.head.value == '2018'
    assert list.head.next_.value == '2019'
    

def test_all_values():
    list = LinkedList()
    list.insert('2020')
    list.insert('2019')
    list.insert('2018')
    assert str(list) == 'Head: 2018 : 2019 : 2020 : None'
