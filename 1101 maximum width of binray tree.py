"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree(self, root):
        # Write your code here
        if not root:
            return 0 
        
        queue = deque([(root, 0)])
        res = 0
        while queue:
            width = 0
            left = 0
            right = 0
            length = len(queue)
            for i in range(length):
                cur, index = queue.popleft()
                if cur.left:
                    queue.append((cur.left, index * 2 + 1))
                if cur.right:
                    queue.append((cur.right, index * 2 + 2))
                
                if i == 0:
                    left = index 
                if i == length - 1:
                    right = index 
                    
                width = right - left + 1 
            res = max(res, width)
        return res 