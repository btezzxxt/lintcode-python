"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        if l1 == None:
            return l2
            
        if l2 == None:
            return l1
        
        p1 = l1 
        p2 = l2
        
        dummy = ListNode(-1)
        
        offset = 0
        cur = dummy
        while p1 and p2:
            total = p1.val + p2.val + offset
            if total >= 10:
                offset = 1
                total = total - 10
            else:
                offset = 0
            cur.next = ListNode(total)
            cur = cur.next
            p1 = p1.next 
            p2 = p2.next 
        
        while p1:
            total = p1.val + offset
            if total == 10:
                offset = 1 
                total = total - 10
            else:
                offset = 0 
            cur.next = ListNode(total)
            cur = cur.next 
            p1 = p1.next
            
        while p2:
            total = p2.val + offset
            if total == 10:
                offset = 1 
                total = total - 10 
            else:
                offset = 0 
            cur.next = ListNode(total)
            cur = cur.next
            p2 = p2.next 
        
        if offset == 1:
            cur.next = ListNode(offset)
        return dummy.next
