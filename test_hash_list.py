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

