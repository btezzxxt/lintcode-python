"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: all the values with the highest frequency in any order
    """
    def findFrequentTreeSum(self, root):
        # Write your code here
        if not root:
            return []
        
        val_count = {}
        self.dfs(root, val_count)
        
        arr = [(val, count) for val, count in val_count.items() ]
        arr.sort(key=lambda x: (-x[1], x[0]))
        
        res = []
        max_count = arr[0][1]
        for val, count in arr:
            if count == max_count:
                res.append(val)
            else:
                break 
        return res
        
    def dfs(self, root, val_count):
        if not root:
            return 0 
        
        left = self.dfs(root.left, val_count)
        right = self.dfs(root.right, val_count)
        
        total = left + right + root.val 
        count = val_count.get(total, 0)
        val_count[total] = count + 1 
        return total 
        