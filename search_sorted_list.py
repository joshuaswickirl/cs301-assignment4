#   
#   1. Search sorted list function
#

def search_sorted_list(sorted_list, item):
    """
    Determines if the item is in the sorted list in log(n) time
    using a binary search algorithm.
    """
    
    item_found = False
    start = 0
    end = len(sorted_list) - 1

    if sorted_list[start] > item or sorted_list[end] < item:
        return False
    
    while not item_found:
        mid = (end - start)//2 + start
        if sorted_list[mid] == item:
            item_found = True
        elif start == end-1:
            if sorted_list[end] == item:
                item_found = True
            break
        elif sorted_list[mid] > item:
            start = start
            end = mid
        elif sorted_list[mid] < item:
            start = mid
            end = end

    return item_found
