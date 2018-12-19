"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        return self.findLCAorAB(root, A, B)[0]

    # return LCA, findA, findB 
    def findLCAorAB(self, root, A, B):
        if root is None:
            return None, False, False
        l_lca, l_a, l_b = self.findLCAorAB(root.left, A, B)
        r_lca, r_a, r_b = self.findLCAorAB(root.right, A, B)

        if l_lca:
            return l_lca, True, True

        if r_lca:
            return r_lca, True, True
        
        if (l_a and r_b) or (l_b and r_a):
            return root, True, True
        
        if root == A and (l_b or r_b):
            return root, True, True
        
        if root == B and (l_a or r_a):
            return root, True, True

        if root == A and root == B:
            return root, True, True

        if l_a or r_a or root == A:
            return None, True, False
        
        if l_b or r_b or root == B:
            return None, False, True
        
        return None, False, False
        

