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

# 非递归 用栈， 先入右边 再压入左边 最后把root右边连上栈顶元素，左边清零
# """
# Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None
# """

# class Solution:
#     """
#     @param root: a TreeNode, the root of the binary tree
#     @return: nothing
#     """
#     def flatten(self, root):
#         if not root:
#             return root
        
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.right:
#                 stack.append(node.right)
            
#             if node.left:
#                 stack.append(node.left)
                
#             node.left = None
#             if stack:
#                 node.right = stack[-1]
#             else:
#                 node.right = None
        

