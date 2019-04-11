class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return self.helper(root, A, B)
        
    # if found A, return A, else B else LCA, else None 
    def helper(self, root, A, B):
        if not root:
            return None 
            
        if root == A:
            return A 
        
        if root == B:
            return B 
        
        l_found = self.helper(root.left, A, B)
        r_found = self.helper(root.right, A, B)
        
        if not l_found and not r_found:
            return None 
        elif not l_found:
            return r_found
        elif not r_found:
            return l_found 
        else:
            return root
            
            
            
            