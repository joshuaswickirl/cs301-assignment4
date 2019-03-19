#
#
#

def search_sorted_list(sorted_list, item):
    """
    Determines if the item is in the sorted list in log(n) time
    using a binary search algorithm.
    """
    
    item_found = False
    start = 0
    end = len(sorted_list)
    mid = end // 2
    
    while not item_found:
        half_list = sorted_list[start:mid]
        if sorted_list[start] > item:
            break
        elif item in half_list:
            item_found = True
            break
        elif start == end-1:
            if sorted_list[end-1] == item:
                item_found = True
            break
        else:
            start = mid
            mid = (end + mid) // 2

    return item_found
