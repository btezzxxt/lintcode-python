"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        len1, len2 = 0, 0
        p1, p2 = headA, headB
        
        while p1:
            len1 += 1 
            p1 = p1.next 
        
        while p2:
            len2 += 1 
            p2 = p2.next 
        
        p1, p2 = headA, headB
        if len1 > len2:
            diff = len1 - len2
            while diff > 0:
                p1 = p1.next
                diff -= 1 
        else:
            diff = len2 - len1
            while diff > 0:
                p2 = p2.next
                diff -= 1
                
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1