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
    @param index: index.
    @param value: value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.max = value
            return root.max
        
        max_left, max_right = -sys.maxsize, -sys.maxsize
        mid = (root.start + root.end) // 2
        if index <= mid:
            max_left = self.modify(root.left, index, value)
            if root.right:
                max_right = root.right.max
        elif index > mid:
            if root.left:
                max_left = root.left.max
            max_right = self.modify(root.right, index, value)
        root.max = max(max_left, max_right)
        return root.max
        
        