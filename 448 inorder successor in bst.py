"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
#1 按path 不管bst
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        stack = []
        while root != p:
            stack.append(root)
            if root.val > p.val:
                root = root.left 
            if root.val < p.val:
                root = root.right
                
        if p.right:
            cur = p.right
            while cur:
                stack.append(cur)
                cur = cur.left
        else:
            cur = p 
            while stack and stack[-1].right == cur:
                cur = stack.pop()
        return stack[-1] if stack else None

#2 非递归
class Solution2:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        succ = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                if not succ or root.val < succ.val:
                    succ = root 
                root = root.left 
        return succ
            
# 递归
class Solution3:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return None 
        
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            succ = self.inorderSuccessor(root.left, p)
            if succ and succ.val < root.val:
                return succ
            return root