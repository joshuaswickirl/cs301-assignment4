#
#   5. Sort list function
#

def sort_list(ulist):
    length = len(ulist)
    sortedList = []
    minimum = None
    for i in range (length):
        for j in range (length):
            if ulist[j] < ulist[i]:
                minimum = ulist[j]
        sortedList.append(minimum)
        minimum = ulist[i]
    return sortedList
