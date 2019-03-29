"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        if head == None or head.next == None:
            return head 
        
        dummy = ListNode(-1)
        p1 = dummy 
        p2 = head
        p3 = head.next
        while p2 and p3:
            p2.next = p3.next
            p1.next = p3 
            p3.next = p2
            
            p1 = p2
            p2 = p2.next
            p3 = p2.next if p2 else None

        return dummy.next 
