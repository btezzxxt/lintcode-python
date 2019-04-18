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
    def longestConsecutive2(self, root):
        # write your code here
        _, res, _, _ = self.dfs(root)
        return 

    # @return local max lenth, global max, pass_root?, root_val
    def dfs(self, root):
        if root is None:
            return 0, False, 0
        
        l_local, l_global, l_p_root, l_val = self.dfs(root.left)
        r_local, r_global, r_p_root, r_val = self.dfs(root.right)

        if l_p_root and r_p_root:
            if root.val == l_local + 1:
                local_max = l_local + 1 
                global_max = max(l_global, local_max, r_global)
            
            if root.val == r_local + 1:
                local_max = r_local + 1
                global_max = max(l_global, local_max, r_global)

            
            if root.val != l_local + 1 or root.val != r_local + 1:
                local_max = 1
                return local_max, global_max, False, root.val
            return local_max, global_max, True, root.val
        elif l_p_root:
            if root.val == l_local + 1:
                local_max = l_local + 1
                global_max = max(l_global, local_max, r_global)
                return local_max, global_max, True, root.val
            else:
                local_max = 1
                global_max = max(l_global, local_max, r_global)
                return local_max, global_max, False, root.val
        elif r_p_root:
            if root.val == r_local + 1:
                local_max = r_local + 1
                global_max = max(l_global, local_max, r_global)
                return local_max, global_max, True, root.val
            else:
                local_max = 1 
                global_max = max(l_global, local_max, r_global)
                return local_max, global_max, False, root.val
        else:
            local_max = 1
            global_max = max(l_global, local_max, r_global)
            return local_max, global_max, False, root.val


        
                        
