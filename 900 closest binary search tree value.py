"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    # 深度优先搜索 分治法经典
    def closestValue(self, root, target):
        # write your code here
        node, minGap = self.findClosest(root, target)
        return node.val
    
    def findClosest(self, root, target):
        if root == None:
            return None, sys.maxsize
        
        nodeL, gapL = self.findClosest(root.left, target)
        nodeR, gapR = self.findClosest(root.right, target)

        if gapL == min(gapL, gapR, abs(target - root.val)):
            return nodeL, gapL
        if gapR == min(gapL, gapR, abs(target - root.val)):
            return nodeR, gapR
        return root, abs(target - root.val)

        