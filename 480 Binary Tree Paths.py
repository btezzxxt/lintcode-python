"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        res = []
        self.findAllPath(root, [], res)
        return res
    
    def findAllPath(self, root, path, res):
        if root == None:
            return 
        if root and root.left == None and root.right == None:
            path.append(str(root.val))
            string = "->".join(path)
            path.pop()
            res.append(string)
            return
        
        path.append(str(root.val))
        self.findAllPath(root.left, path, res)
        self.findAllPath(root.right, path, res)
        path.pop()
        