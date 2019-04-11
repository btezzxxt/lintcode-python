"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# 非递归
# class Solution:
#     """
#     @param root: the given BST
#     @param p: the given node
#     @return: the in-order predecessor of the given node in the BST
#     """
#     def inorderPredecessor(self, root, p):
#         # write your code here
#         succ = None
#         while root:
#             if root.val >= p.val:
#                 root = root.left 
#             else:
#                 if (not succ or root.val > succ.val):
#                     succ = root 
#                 root = root.right 
#         return succ


# 递归
class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        if not root:
            return None
        
        if p.val <= root.val:
            return self.inorderPredecessor(root.left, p)
        else:
            pre = self.inorderPredecessor(root.right, p)
            if pre and pre.val > root.val:
                return pre
            return root

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 不管bst
class Solution2:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        stack = []
        cur = root
        while cur != p:
            stack.append(cur)
            if cur.val < p.val:
                cur = cur.right 
            else:
                cur = cur.left
        
        if p.left:
            cur = p.left
            while cur:
                stack.append(cur)
                cur = cur.right 
            return stack[-1] if stack else None
        else:
            while stack and stack[-1].left == cur:
                cur = stack.pop()
            return stack[-1] if stack else None        