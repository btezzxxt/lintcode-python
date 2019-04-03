class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None



class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        self.copy_next(head)
        self.copy_random(head)
        new_head = self.split_list(head)
        return new_head
        
    def copy_next(self, head):
        while head:
            new = RandomListNode(head.label)
            new.next = head.next
            head.next = new 
            head = head.next.next 
        
    def copy_random(self, head):
        while head:
            new = head.next 
            if head.random:
                new.random = head.random.next
            head = head.next.next 
    
    def split_list(self, head):
        if not head:
            return None
        
        dummy = RandomListNode(-1)
        dummy.next = head.next
        new = dummy.next
        head.next = head.next.next
        head = head.next
        
        while head:
            new.next = head.next
            head.next = head.next.next
            head = head.next 
            new = new.next
        return dummy.next
            
one = RandomListNode(-1)
two = RandomListNode(1)
one.next = two 

Solution().copyRandomList(one)