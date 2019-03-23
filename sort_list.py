#
#   5. Sort list function
#

def sort_list(ulist):
    """
    Returns sorted numerical list.
    """
    length = len(ulist)
    sorted_list = []
    sorted_list.insert(0,ulist[0])
    for item in ulist[1:]:
        index = 0
        index_found = False
        if item < sorted_list[index]:
            sorted_list.insert(index,item)
            index_found = True
        while not index_found:
            if index == len(sorted_list)-1:
                sorted_list.append(item)
                index_found = True
            elif item > sorted_list[index] and item < sorted_list[index+1]:
                sorted_list.insert(index+1,item)
                index_found = True
            else:
                index += 1
    return sorted_list
    