class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return head 
        
        dummy = ListNode(-1)
        dummy.next = head
        head, tail = self.reverse_first_k(head, k)
        dummy.next = head 
        if tail:
            tail.next = self.reverseKGroup(tail.next, k)
        return dummy.next
    
    def reverse_first_k(self, head, k):
        if not head or not head.next:
            return head, head
        
        dummy = ListNode(-1)
        dummy.next = head 
        
        count = 0
        while head and count < k:
            count += 1 
            head = head.next
        if count < k:
            return dummy.next, None
            
        next_head = head
        
        p1 = dummy.next 
        p2 = p1.next 
        while p2 != next_head:
            p1.next = p2.next 
            p2.next = dummy.next
            dummy.next = p2
            p2 = p1.next
        
        return dummy.next, p1

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2 
l2.next = l3 
l3.next = l4 
l4.next = l5

Solution().reverseKGroup(l1, 3)






        
                
        