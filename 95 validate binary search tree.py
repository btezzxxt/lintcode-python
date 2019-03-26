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

class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        valid, _, _ = self.helper(root)
        return valid
    
    def helper(self, root): 
        if root == None:
            return True, None, None
        
        # 最后处理叶子结点
        left_valid, left_min, left_max = self.helper(root.left)
        right_valid, right_min, right_max = self.helper(root.right)
        
        if not left_valid or not right_valid:
            return False, None, None
        
        # left exists and right exists
        if left_max and right_min:
            if left_max.val < root.val and root.val < right_min.val:
                return True, left_min, right_max
            else:
                return False, None, None
        # only left exists
        elif left_max:
            if left_max.val < root.val:
                return True, left_min, root
            else:
                return False, None, None
        # only right exists
        elif right_min:
            if root.val < right_min.val:
                return True, root, right_max
            else:
                return False, None, None
        # leaf node
        else:
            return True, root, root
        
        
        
        
            