
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        newnode = ListNode(x)
        if not node:
            newnode.next = newnode
            return newnode
            
        anchor = node 
        big = node
        node = node.next 
        while node and node != anchor:
            if node.val >= big.val and (not node.next or node.next.val < node.val):
                big = node
            node = node.next
        
        small = big.next
        if x >= big.val or x <= small.val:
            newnode.next = big.next 
            big.next = newnode   
        else:
            while small.next.val < x:
                small = small.next
            newnode.next = small.next 
            small.next = newnode
        return newnode