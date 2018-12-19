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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced = self.helper(root)
        return is_balanced[0]
    
    # check subtree balanced, return isBalanced, height
    def helper(self, root):
        if root is None:
            return True, 0
        
        left_bal, left_h = self.helper(root.left)
        right_bal, right_h = self.helper(root.right)

        if not left_bal or not right_bal:
            return False, 0
        
        h_diff = abs(left_h - right_h)
        if h_diff > 1:
            return False, 0
        else:
            return True, max(right_h, left_h) + 1