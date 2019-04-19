"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        _, longest = self.helper(root)
        return longest - 1 
    
    # local max depth from root to a leaf, global max
    def helper(self, root):
        if not root:
            return 0, 0
            
        l_depth, l_global = self.helper(root.left)
        r_depth, r_global = self.helper(root.right)
        
        depth = max(l_depth, r_depth) + 1
        g = max(l_depth + 1 + r_depth, l_global, r_global)
        return depth, g