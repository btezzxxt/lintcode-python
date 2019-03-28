"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
        
        p1 = None
        p2 = head
        p3 = head.next
        
        while p3 != None:
            # revert p2
            # None -> 1 -> 2 -> 3
            #  p1     p2   p3
            
            p2.next = p1
            p1 = p3.next
            # None <- 1 -> 2 -> 3 
            #         p2  p3  p1
            
            p1, p2, p3 = p2, p3, p1
            # re-label for the next round. to modify p2 still
            # None <- 1 -> 2 -> 3 
            #         p1  p2   p3            
        
        # 2 -> 3 -> None
        # p1   p2   p3
        p2.next = p1 
        return p2