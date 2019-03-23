#
#   2. Hash list class
#

class HashList():

    def __init__(self, length):
        """
        Creates a new empty HashList of the given length.
        """
        self.hash_list = [None] * length
        self.hash_length = length

    
    def hashfunction(self, item):
        """
        Tells you which slot the item should be assigned to.
        """
        return item % self.hash_length


    def put(self, item):
        """
        Adds the given item to the list.
        If the list is full, raises an error.
        """
        index = self.hashfunction(item)
        empty_index = False
        slots_checked = 0
        while not empty_index:
            if self.hash_list[index] == None:
                self.hash_list.insert(index,item)
                empty_index = True
            elif index == self.hash_length - 1:
                index = 0
                slots_checked += 1
            elif slots_checked == self.hash_length:
                raise RuntimeError
            else:
                index += 1
                slots_checked += 1


    def contains(self, item):
        """
        Returns True if the given item is in the list; False otherwise.
        """
        contains_item = False
        slots_checked = 0
        index = self.hashfunction(item)
        while not contains_item:
            if self.hash_list[index] == item:
                contains_item = True
            elif index == self.hash_length - 1:
                index = 0
                slots_checked += 1
            elif slots_checked == self.hash_length:
                break
            else:
                index += 1
                slots_checked += 1
        return contains_item


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