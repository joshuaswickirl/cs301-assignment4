import env
import pytest

from hash_list import HashList

#
#   Tests for HashList class
#

# HashList.hashfunction(item)
def test_hashfunction_1():
    list_length = 10
    item = 10
    _hashlist = HashList(list_length)
    assert _hashlist.hashfunction(item) == 0

def test_hashfunction_2():
    list_length = 10
    item = 32
    _hashlist = HashList(list_length)
    assert _hashlist.hashfunction(item) == 2

# HashList.put(item)
def test_put_1():
    list_length = 10
    item = 32
    _hashlist = HashList(list_length)
    _hashlist.put(item)
    assert _hashlist.hash_list[2] == 32

def test_put_2():
    list_length = 10
    item = 53
    _hashlist = HashList(list_length)
    _hashlist.put(item)
    assert _hashlist.hash_list[3] == 53

def test_put_3():
    list_length = 10
    item1 = 10
    item2 = 59
    item3 = 69
    _hashlist = HashList(list_length)
    _hashlist.put(item1)
    _hashlist.put(item2)
    _hashlist.put(item3)
    assert _hashlist.hash_list[1] == 69

# HashList.contains(item)
def test_contains_1():
    list_length = 10
    item = 10
    _hashlist = HashList(list_length)
    _hashlist.put(item)
    assert _hashlist.contains(item) == True

def test_contains_2():
    list_length = 10
    item1 = 10
    item2 = 59
    item3 = 69
    _hashlist = HashList(list_length)
    _hashlist.put(item1)
    _hashlist.put(item2)
    _hashlist.put(item3)
    assert _hashlist.contains(item3) == True

def test_contains_3():
    list_length = 10
    item1 = 10
    item2 = 59
    item3 = 69
    _hashlist = HashList(list_length)
    _hashlist.put(item1)
    _hashlist.put(item2)
    _hashlist.put(item3)
    assert _hashlist.contains(11) == False

# HashList.items()
def test_items_1():
    list_length = 10
    item1 = 10
    item2 = 59
    item3 = 69
    _hashlist = HashList(list_length)
    _hashlist.put(item1)
    _hashlist.put(item2)
    _hashlist.put(item3)
    assert _hashlist.items() == [10,69,59]

def test_items_2():
    list_length = 10
    items = [1,2,3,4,5,6,7,8,9]
    _hashlist = HashList(list_length)
    for item in items:
        _hashlist.put(item)
    assert _hashlist.items() == items