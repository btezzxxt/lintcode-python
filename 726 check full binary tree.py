"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: Whether it is a full tree
    """
    def isFullTree(self, root):
        # write your code here
        if not root:
            return True
        
        if not root.left and root.right:
            return False 
        
        if root.left and not root.right:
            return False 
        
        return self.isFullTree(root.left) and self.isFullTree(root.right)

