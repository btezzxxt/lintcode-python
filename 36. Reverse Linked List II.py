"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
"""
Reverse a linked list from position m to n.

Example
Example 1:

Input: 1->2->3->4->5->NULL, m = 2 and n = 4, 
Output: 1->4->3->2->5->NULL.
Example 2:

Input: 1->2->3->4->NULL, m = 2 and n = 3, 
Output: 1->3->2->4->NULL.
Challenge
Reverse it in-place and in one-pass

Notice
Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.
"""


class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or not head.next:
            return head 
        
        if m == n:
            return head 
        
        dummy = ListNode(-1)
        dummy.next = head
        count = 0
        
        while count + 1 < m:
            dummy = dummy.next 
            count += 1 
        
        p1 = dummy.next 
        p2 = dummy.next.next 

        times = n - m 
        for _ in range(times):
            p1.next = p2.next 
            p2.next = dummy.next 
            dummy.next = p2 

            p2 = p1.next 
        
        return head if m != 1 else dummy.next

