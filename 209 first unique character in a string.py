class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        helper = FirstUniqCharHandler()
        for c in str:
            helper.add(c)
        return helper.getFirstUniq().val


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class FirstUniqCharHandler:
    def __init__(self):
        self.DUMMY_HEAD = LinkedListNode(0)
        self.tail = self.DUMMY_HEAD
        # key saves the location of each character
        # value saves previous node 
        self.map = {}

        # duplicated characters
        self.duplicate = set()

    def add(self, c):
        if c in self.duplicate:
            return
        
        if c in self.map:
            self.duplicate.add(c)
            self.remove(c)
        else:
            self.tail.next = LinkedListNode(c)
            self.map[c] = self.tail
            self.tail = self.tail.next
    
    def getFirstUniq(self):
        return self.DUMMY_HEAD.next
    
    def remove(self, c):
        pre = self.map[c]
        if pre.next:
            pre.next = pre.next.next
        
        del self.map[c]
        
        if pre.next:
            self.map[pre.next.val] = pre
        # if pre.next is none means pre is tail
        else:
            self.tail = pre


print(Solution().firstUniqChar("aabc"))
        




    