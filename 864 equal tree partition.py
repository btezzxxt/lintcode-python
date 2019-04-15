"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        # write your code here
        if not root or (not root.left and not root.right):
            return False
        
        total = self.get_sum(root)
        
        left_check, _ = self.check(root.left, total)
        right_check, _ = self.check(root.right, total)
        return left_check or right_check 
        
    def check(self, root, total):
        if not root:
            return False, 0 
        
        left_check, left_sum = self.check(root.left, total)
        right_check, right_sum = self.check(root.right, total)
        
        if left_check or right_check:
            return True, 0 
        
        local_sum = left_sum + root.val + right_sum 
        if local_sum == total - local_sum:
            return True, 0 
        return False, local_sum 
        
    def get_sum(self, root):
        if not root:
            return 0 
        
        left = self.get_sum(root.left)
        right = self.get_sum(root.right)
        return left + root.val + right