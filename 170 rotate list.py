"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head:
            return head
        
        n = self.count(head)
        if k >= n:
            k %= n
        
        if k == 0:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head 
        
        p1 = dummy
        step = n - k 
        while step > 0:
            p1 = p1.next
            step -= 1 
            
        p2 = p1.next
        p1.next = None 
        p1 = dummy.next 
        dummy.next = p2
        
        while p2.next != None:
            p2 = p2.next
        p2.next = p1 
        return dummy.next
        
    def count(self, head):
        if not head:
            return 0
        
        n = 0
        while head:
            n += 1 
            head = head.next 
        return n
        