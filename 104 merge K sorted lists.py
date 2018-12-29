
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

from heapq import heappush, heappop
# autoincrease counter for heap lt tie breaker before object
import itertools
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        counter = itertools.count()
        heap = []
        for node in lists:
            if node:
                heappush(heap, (node.val, next(counter), node))
        
        DUMMY_HEAD = ListNode(0)
        tail = DUMMY_HEAD
        while heap:
            _, node = heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heappush(heap, (node.next.val, next(counter), node.next))
        
        return DUMMY_HEAD.next



