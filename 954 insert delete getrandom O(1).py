import collections
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [] 
        self.val_idx = collections.defaultdict(list)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.arr.append(val)
        self.val_idx[val].append(len(self.arr) - 1)
        return True
            
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_idx or len(self.val_idx[val]) == 0:
            return False
        
        index = self.val_idx[val].pop()
        if index == len(self.arr) - 1:
            self.arr.pop()
        else:
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.val_idx[self.arr[index]].pop()
            self.val_idx[self.arr[index]].append(index)
            self.arr.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        rand = random.randint(0, len(self.arr) - 1)
        return self.arr[rand]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()