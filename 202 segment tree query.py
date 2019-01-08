"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if start == root.start and end == root.end:
            return root.max

        max_left, max_right = -sys.maxsize, - sys.maxsize
        mid_of_root = (root.start + root.end) // 2
        if start <= mid_of_root:
            max_left = self.query(root.left, start, min(mid_of_root, end))
        
        if end > mid_of_root:
            max_right = self.query(root.right, max(start, mid_of_root + 1), end)
        
        return max(max_left, max_right)

        
