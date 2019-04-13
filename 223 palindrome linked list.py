class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if not head:
            return True 
            
        left_start = head 
        p1 = head 
        p2 = head 
        
        while p2.next and p2.next.next:
            p1 = p1.next 
            p2 = p2.next.next
        
        # even 
        right_end = None 
        if p2.next:
            right_end = p1.next 
        # odd
        else:
            right_end = p1
        
        right_start = self.reverse_linkedlist(right_end)
        
        while left_start and right_start:
            if left_start.val != right_start.val:
                return False 
            left_start = left_start.next 
            right_start = right_start.next
            
        return True
        
    def reverse_linkedlist(self, head):
        if not head or not head.next:
            return head 
            
        dummy = ListNode(-1)
        dummy.next = head
        p1 = head
        p2 = head.next
        while p2:
            p1.next = p2.next
            p2.next = dummy.next
            dummy.next = p2
            p2 = p1.next
        
        return dummy.next
        
a = ListNode(1)
b = ListNode(1)
c = ListNode(0)
d = ListNode(0)
e = ListNode(1)
        
a.next = b 
b.next = c 
c.next = d 
d.next = e
Solution().isPalindrome(a)