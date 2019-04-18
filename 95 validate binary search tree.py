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
        
        
        
        
class Solution:
    # def isValidBST(self, root):
    #     valid, _, _ = self.dfs(root)
    #     return valid
    
    # #@ return is valid, smallest, biggest
    # def dfs(self, root):
    #     if not root:
    #         return True, None, None
        
    #     if not root.left and not root.right:
    #         return True, root.val, root.val
        
    #     left_valid, left_small, left_big = self.dfs(root.left)
    #     right_valid, right_small, right_big = self.dfs(root.right)

    #     if left_valid and right_valid:
    #         if (not left_big or left_big < root.val) and (not right_small or root.val < right_small):
    #             left_val = left_small if left_small else root.val
    #             right_val = right_big if right_big else root.val 
    #             return True, left_val, right_val 
    #     return False, None, None

    def isValidBST(self, root):
        if not root:
            return True 
        
        stack = []
        while root:
            stack.append(root)
            root = root.left 

        pre = None 
        while stack:
            node = stack.pop()
            if pre != None and node.val <= pre.val:
                return False

            if node.right:
                cur = node.right
                while cur:
                    stack.append(cur)
                    cur = cur.left 
            else:
                cur = node
                while stack and stack[-1].right == cur:
                    cur = stack.pop()
            pre = node

        return True