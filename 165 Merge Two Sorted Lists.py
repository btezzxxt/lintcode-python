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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2 
        
        if l2 is None:
            return l1 
        
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next 
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next 
        
        while l1:
            cur.next = l1
            l1 = l1.next 
            cur = cur.next 
        
        while l2:
            cur.next =l2
            l2 = l2.next 
            cur = cur.next 
            
        return dummy.next
            