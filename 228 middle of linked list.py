"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
        
        slow = head
        fast = head.next # be careful

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        return slow
