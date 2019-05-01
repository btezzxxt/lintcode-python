"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
        
        target_map = set()
        res = []
        self.inorder(root, target_map, n, res)
        print(res)
        return res
    
    def inorder(self, root, target_map, n, res):
        if not root:
            return 
        
        self.inorder(root.left, target_map, n, res)
        if root.val in target_map:
            if len(res) == 0:
                res.append(n - root.val)
                res.append(root.val)
        target_map.add(n - root.val)
        self.inorder(root.right, target_map, n, res)
        
            
        
        