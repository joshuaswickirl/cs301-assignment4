#
#   2. Hash list class
#

class HashList():

    def __init__(self, length):
        """
        Creates a new empty HashList of the given length.
        """
        self.hash_list = [None] * length

    
    def hashfunction(self, item):
        """
        Finds the index for the given item.
        """
        item_index = 0
        item_found = False
        for list_item in self.hash_list:
            if list_item == item:
                item_found = True
                break
            else:
                item_index += 1
        if not item_found:
            raise IndexError
        return item_index


    def put(self, item):
        """
        Adds the given item to the list.

        If the list is full, raises an error.
        """
        pass


    def contains(self, item):
        """
        Returns True if the given item is in the list; False otherwise.
        """
        pass


    def items(self):
        """
        Returns a list of all items in the HashList.
        """
        pass


#
#   3. Explain the running times of the HashList methods
#      in both the best-case scenario and worst-case scenario.
#
#


#
#   4. How would we convert the HashList into a dictionary?
#
#