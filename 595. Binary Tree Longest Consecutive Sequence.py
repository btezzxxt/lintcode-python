"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.dfs(None, root, 0, 0)

    def dfs(self, prev, root, local_max, global_max):
        if root == None:
            return global_max
        
        if prev == None:
            local_max = 1 
            global_max = 1 
        else:
            if prev.val + 1 == root.val:
                local_max += 1 
                global_max = max(local_max, global_max)
            else:
                local_max = 1 

        left_val = self.dfs(root, root.left, local_max, global_max)
        right_val = self.dfs(root, root.right, local_max, global_max)
        return max(left_val, right_val)


