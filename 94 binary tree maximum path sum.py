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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        _, max_sum = self.dfs(root)
        return max_sum

    # return max_sum of root to end; max_sum of tree
    def dfs(self, root):
        if root == None:
            return -sys.maxsize, -sys.maxsize

        if root.left == None and root.right == None:
            return root.val, root.val
        
        l_root_sum, l_max_sum = self.dfs(root.left)
        r_root_sum, r_max_sum = self.dfs(root.right)

        root_sum = max(l_root_sum + root.val, r_root_sum + root.val, root.val)
        max_sum = max(l_root_sum + root.val + r_root_sum, \
            root_sum, l_max_sum, r_max_sum)
            
        return root_sum, max_sum