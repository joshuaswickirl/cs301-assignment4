import pytest

from sort_list import sort_list

#
#   Tests for sort_list()
#

def test_sort_list_1():
    ulist = [3,2,1]
    assert sort_list(ulist) == [1,2,3]

def test_sort_list_2():
    ulist = [1,4,5,9,2,15,0]
    assert sort_list(ulist) == [0,1,2,4,5,9,15]

def test_sort_list_3():
    ulist = [21,9,-1,4]
    assert sort_list(ulist) == [-1,4,9,21]