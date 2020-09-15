from hashtable import Hashtable


def test_hashtable_default_size():
    hashtable = Hashtable()
    expected = 1024
    actual = hashtable.size
    assert actual == expected


def test_hashtable_size_58_pass():
    hashtable = Hashtable(58)
    expected = 58
    actual = hashtable.size
    assert actual == expected


def test_hashtable_size_58_fail():
    hashtable = Hashtable(58)
    expected = 57
    actual = hashtable.size
    assert actual != expected


def test_single_hash_pass():
    hashtable = Hashtable()
    hashtable.add('roger', 45)
    actual = hashtable.get('roger')
    expected = 45
    assert actual == expected


def test_single_hash_fail():
    hashtable = Hashtable()
    hashtable.add('roger', 45)
    actual = hashtable.get('roger')
    expected = 44
    assert actual != expected

def test_contains_true():
    hashtable = Hashtable()
    hashtable.add('roger', 45)
    actual = hashtable.contains('roger')
    expected = True
    assert actual == expected

def test_contains_false():
    hashtable = Hashtable()
    hashtable.add('roger', 45)
    actual = hashtable.contains('roger')
    expected = False
    assert actual == expected