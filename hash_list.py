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