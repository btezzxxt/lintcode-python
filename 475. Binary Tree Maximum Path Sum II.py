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
    @param root: the root of binary tree.
    @return: An integer
    """
    max_val = -sys.maxsize

    def maxPathSum2(self, root):
        # write your code here
        self.dfs(root, 0)
        return self.max_val

    def dfs(self, root, total):
        if not root:
            return 

        total += root.val
        self.max_val = max(self.max_val, total)

        self.dfs(root.left, total)
        self.dfs(root.right, total)


# 1 2 3