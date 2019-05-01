
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Example
Example 1:
	Input:  1->2->3->4->null
	Output: 1->4->2->3->null

Example 2:
	Input: 1->2->3->4->5->null
	Output: 1->5->2->4->3->null
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head:
            return head 
            
        if not head.next:
            return head 
        
        slow = head 
        fast = head 

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next 
        
        second_head = slow.next 
        slow.next = None 
        second_head = self.reverse(second_head)
        first_head = head

        dummy = ListNode(-1)
        tail = dummy 

        while first_head and second_head:
            tail.next = first_head
            first_head = first_head.next 
            tail = tail.next 

            tail.next = second_head
            second_head = second_head.next 
            tail = tail.next 
        
        if first_head:
            tail.next = first_head
        return dummy.next
    
    def reverse(self, head):
        dummy = ListNode(-1)
        dummy.next = head 

        p1 = head 
        p2 = head.next 

        while p1 and p2:
            p1.next = p2.next
            p2.next = dummy.next 
            dummy.next = p2 

            p2 = p1.next 
        
        return dummy.next
