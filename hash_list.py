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
                self.hash_list[index] = item
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
        slots_searched = 0
        index = self.hashfunction(item)
        while not contains_item:
            if self.hash_list[index] == item:
                contains_item = True
            elif self.hash_list[index] == None:
                break
            elif slots_searched >= self.hash_length-1:
                break
            elif index == self.hash_length - 1:
                index = 0
                slots_searched += 1
            else:
                index += 1
                slots_searched += 1
                
        return contains_item


    def items(self):
        """
        Returns a list of all items in the HashList.
        """
        list_o_items = []
        for item in self.hash_list:
            if item == None:
                continue
            else:
                list_o_items.append(item)
        return list_o_items


#
#   3. Explain the running times of the HashList methods
#      in both the best-case scenario and worst-case scenario.
#
#   .hashfunction
#       Best-case and worst-case scenario this method 
#       runs in constant time.
#
#   .put
#       Best-case runs in constant time, worst-case runs in 
#       linear time.
#
#   .contains
#       Best-case scenario this function runs in constant time 
#       and worst-case scenario this function runs in linear time.
#   
#   .items 
#       Best-case and worst-case run in linear time.
#   


#
#   4. How would we convert the HashList into a dictionary?
#
#   We would convert the HashList into a dictionary by using
#   what is returned by the .hashfunction as the key and the 
#   item in the associated slot as the value.
#