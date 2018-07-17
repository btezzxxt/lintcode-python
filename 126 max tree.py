# test = [2,5,7,0,3,1,6]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from Printer import Printer 
class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        stack = []
        if len(A) == 0:
            return None
        
        for num in A:
            node = TreeNode(num) 
            if not stack:
                stack.append(node)
            else:
                if stack[-1].val > node.val:
                    stack[-1].right = node
                    stack.append(node)
                else:
                    while stack and stack[-1].val < node.val:
                        node.left = stack.pop()
                    if stack:
                        stack[-1].right = node
                    stack.append(node)
        
        while stack:
            root = stack.pop()

        return root

root = Solution().maxTree([2,5,7,0,3,1,6])
Printer.tree(root)

