class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.parent_map = {}
        self.duplicate = set()
        self.head = LinkedList(None)
        self.tail = self.head
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num in self.duplicate:
            return 
        
        if num not in self.parent_map:
            self.tail.next = LinkedList(num)
            self.parent_map[num] = self.tail
            self.tail = self.tail.next
        else:
            self.remove_from_list(num)
            del self.parent_map[num]
            self.duplicate.add(num)
    
    def remove_from_list(self, num):
        pre = self.parent_map[num]
        pre.next = pre.next.next
        if pre.next:
            self.parent_map[pre.next.val] = pre
        else:
            self.tail = pre
    
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        return self.head.next.val