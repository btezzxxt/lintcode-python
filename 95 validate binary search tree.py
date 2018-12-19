"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        isValid, s, l = self.helper(root)
        return isValid

    # return isValid, min, max of a tree
    def helper(self, root):
        if root is None:
            return True, 0, 0 
        
        # deal with leaves
        if root.left is None and root.right is None:
            return True, root.val, root.val
        
        l_valid, l_min, l_max = self.helper(root.left)
        r_valid, r_min, r_max = self.helper(root.right)

        if not l_valid or not r_valid:
            return False, 0, 0
        
        # 一定要考虑只有一边孩子的情况
        if root.right is None and root.val > l_max:
            return True, l_min, root.val

        if root.left is None and root.val < r_min:
            return True, root.val, r_max

        if root.val <= l_max or root.val >= r_min:
            return False, 0, 0
        
        return True, l_min, r_max
