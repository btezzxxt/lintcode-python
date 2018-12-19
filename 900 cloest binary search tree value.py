"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        lower_bound = self.getLowerBound(root, target)
        upper_bound = self.getUpperBound(root, target)

        if lower_bound and upper_bound:
            if abs(lower_bound.val - target) <= abs(upper_bound.val - target):
                return lower_bound.val
            else:
                return upper_bound.val
        elif lower_bound:
            return lower_bound.val
        elif upper_bound:
            return upper_bound.val
        else:
            return -1

    # find an node that's smaller than target
    def getLowerBound(self, root, target):
        if root is None:
            return None
        
        # 如果target 小于或者等于当前节点 在左边寻找，等于不合法
        if target <= root.val:
            return self.getLowerBound(root.left, target)
        # 如果target大于当前节点 有两种情况 1. 在右边找到了一个最小值 2.root就是最小bound
        else:
            right = self.getLowerBound(root.right, target)
            if right:
                return right
            else:
                return root

    # find an node that 's greater or equal to target
    def getUpperBound(self, root, target):
        if root is None:
            return None
        
        if target > root.val:
            return self.getUpperBound(root.right, target)
        else:
            left = self.getUpperBound(root.left, target)
            if left:
                return left
            else:
                return root


