import pytest

from search_sorted_list import search_sorted_list

#
#   Tests for searched_sorted_list()
#

def test_search_sorted_list_1():
    sorted_list = [1,2,3,4,5,6,7,8,9,10]
    item = 9
    assert search_sorted_list(sorted_list,item) == True

def test_search_sorted_list_2():
    sort_list = [10,11,12,13,14,15,16,17,18,19,20]
    item = 9
    assert search_sorted_list(sort_list,item) == False

def test_search_sorted_list_3():
    sort_list = [10,11,12,13,14,15,16,17,18,19,20]
    item = 20
    assert search_sorted_list(sort_list,item) == True

def test_search_sorted_list_4():
    sort_list = [11,13,15,17,19,21,23,25,27,29]
    item = 15
    assert search_sorted_list(sort_list,item) == True