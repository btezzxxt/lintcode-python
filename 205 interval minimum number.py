import sys

class SegmentNode:
    def __init__(self, start, end, min=-sys.maxsize):
        self.start, self.end, self.min = start, end, min
        self.left, self.right = None, None

class SegmentTree:
    def __init__(self, arr):
        self.root = self.build(arr, 0, len(arr) - 1)

    def build(self, arr, start, end):
        if start > end:
            return None
        
        node = SegmentNode(start, end)
        mid = (start + end) // 2
        min_left, min_right = sys.maxsize, sys.maxsize
        if start != end:
            node.left = self.build(arr, start, mid)
            node.right = self.build(arr, mid + 1, end)
            if node.left:
                min_left = node.left.min
            if node.right:
                min_right = node.right.min
            node.min = min(min_left, min_right)
        else:
            node.min = arr[start]
        return node

    def modify(self, node, index, val):
        if node.start == index and node.end == index:
            node.min = val
        
        mid_of_node = (node.start + node.end) // 2
        if index <= mid_of_node:
            min_left = self.modify(node.left, index, val)
            min_right = node.right.min
        if index > mid_of_node:
            min_right = self.modify(node.right, index, val)
            min_left = node.left.min
        node.min = min(min_left, min_right)
        return node.min

    def query_min(self, node, start, end):
        if node.start == start and node.end == end:
            return node.min
        
        min_left, min_right = sys.maxsize, sys.maxsize
        mid_of_node = (node.start + node.end) // 2
        if start <= mid_of_node:
            min_left = self.query_min(node.left, start, min(end, mid_of_node))
        if end > mid_of_node:
            min_right = self.query_min(node.right, max(start, mid_of_node + 1), end)

        return min(min_left, min_right)

        

class Solution:
    """
    @param A: An integer array
    @param queries: An query list
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        tree = SegmentTree(A)
        arr = []
        for q in queries:
            arr.append(tree.query_min(tree.root, q.start, q.end))
        
        return arr