"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        return "".join(self.constructor(t))
    def constructor(self, root):
        if not root:
            return []
            
        res = []
        res.append(str(root.val))
        left = self.constructor(root.left)
        right = self.constructor(root.right)
        
        if not left and not right:
            return res
        elif not left:
            res.append("()(")
            res.extend(right)
            res.append(")")
        elif not right:
            res.append("(")
            res.extend(left)
            res.append(")")
        else:
            res.append("(")
            res.extend(left)
            res.append(")")
            res.append("(")
            res.extend(right)
            res.append(")")
            
        return res
        