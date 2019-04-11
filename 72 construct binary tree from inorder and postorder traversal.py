class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        return self.build_helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
        
    def build_helper(self, inorder, start, end, postorder, p_start, p_end):
        if start > end or p_start > p_end:
            return None
        
        root_val = postorder[p_end]
        index = self.find(inorder, root_val, start, end)
        if index == -1:
            return "broken"
        left_len = index - start
        
        root = TreeNode(root_val)
        root.left = self.build_helper(inorder, start, index - 1, postorder, p_start, p_start + left_len - 1)
        root.right = self.build_helper(inorder, index + 1, end, postorder, p_start + left_len, p_end - 1)
        return root 
    
    def find(self, arr, val, l, r):
        print(arr, l, r, val)
        for i in range(l, r + 1):
            if arr[i] == val:
                return i 
        return -1
Solution().buildTree([2,4,5,3,1], [5,4,3,2,1])

                