"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.helper(root)
        return root

    # 处理node子树并返回last node
    def helper(self, node):
        if node is None:
            return None

        left_last = self.helper(node.left)
        right_last = self.helper(node.right)

        if left_last is None and right_last is None:
            return node

        elif left_last is None:
            return right_last
        
        elif right_last is None:
            node.right = node.left
            node.left = None
            return left_last
        else:
            temp = node.right
            node.right = node.left
            left_last.right = temp
            node.left = None
            return right_last

