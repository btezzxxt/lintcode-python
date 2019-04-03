# from random import randint
# class RandomizedSet:
    
#     def __init__(self):
#         # do intialization if necessary
#         self.arr = []
#         self.map = {}

#     """
#     @param: val: a value to the set
#     @return: true if the set did not already contain the specified element or false
#     """
#     def insert(self, val):
#         # write your code here
#         if val not in self.map:
#             self.arr.append(val)
#             self.map[val] = len(self.arr) - 1

#     """
#     @param: val: a value from the set
#     @return: true if the set contained the specified element or false
#     """
#     def remove(self, val):
#         # write your code here
#         if val not in self.map:
#             return -1 
        
#         index = self.map[val]
#         last_index = len(self.arr) - 1

#         if index != last_index:
#             self.arr[index], self.arr[last_index] = self.arr[last_index], self.arr[index]
#             self.map[self.arr[index]] = index
#         self.arr.pop()
#         del self.map[val]

#     """
#     @return: Get a random element from the set
#     """
#     def getRandom(self):
#         # write your code here
#         index = randint(0, len(self.arr) - 1)
#         return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()

from random import randint
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.arr = []
        self.location_map = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val not in self.location_map:
            self.arr.append(val)
            self.location_map[val] = len(self.arr) - 1
            return True
        else:
            return False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.location_map:
            return False
        else:
            last_index = len(self.arr) - 1 
            val_index = self.location_map[val]
            if last_index == val_index:
                del self.location_map[val]
                self.arr.pop()
            else:
                self.arr[val_index], self.arr[last_index] = self.arr[last_index], self.arr[val_index]
                self.location_map[self.arr[val_index]] = val_index
                del self.location_map[self.arr[last_index]]
                self.arr.pop()
            return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        n = len(self.arr) - 1
        random = randint(0, n)
        return self.arr[random]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()