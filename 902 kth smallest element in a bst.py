class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import sys
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    # 做法三 遍历法 中序遍历iterator
    def kthSmallest(self, root, k):
        if root is None:
            return -1
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        for i in range(k - 1):
            if not stack:
                break
            # 背诵 1. 栈顶为next（）值
            # 2下一个值从栈顶开始，若有右结点，压入栈直到右结点的最左端
            if stack[-1].right:
                node = stack[-1].right
                while node:
                    stack.append(node)
                    node = node.left
            # 3 没有右结点，弹出直到父节点左拐处
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
        return stack[-1]
         
        

    # # 做法二 用一个map记录左右子树结点个数 再做查找 可以反复使用实现o（logh）查找速度
    # def kthSmallest(self, root, k):
    #     count_map = {}
    #     self.countSubtree(root, count_map)
    #     return self.searchKthElement(root, count_map, k)

    # def countSubtree(self, root, count_map):
    #     if root is None:
    #         return 0
        
    #     left_count = self.countSubtree(root.left, count_map)
    #     right_count = self.countSubtree(root.right, count_map)

    #     count_map[root] = left_count + right_count + 1 
    #     return left_count + right_count + 1

    # def searchKthElement(self, root, count_map, k):
    #     if root is None:
    #         return None
        
    #     if root.left is None:
    #         left_count = 0
    #     else:
    #         left_count = count_map[root.left]
        
    #     if k <= left_count:
    #         return self.searchKthElement(root, count_map, k)
    #     if k == left_count + 1:
    #         return root.val
    #     if k > left_count + 1:
    #         return self.searchKthElement(root, count_map, k - left_count - 1)

    # # 做法一： 返回两个值 一个count帮助判断是否找到kth值 一个目标
    # def kthSmallest(self, root, k):
    #     # write your code here
    #     count, kthSmallest = self.helper(root, k)
    #     return kthSmallest.val
    # # 在左子树和右子树中找k，返回子树的node个数和找到的node
    # def helper(self, node, k):
    #     if node is None:
    #         return 0, None
        
    #     # 单独处理叶子结点， 出口一
    #     if node.left is None and node.right is None and k == 1:
    #         return 1, node

    #     l_count, l_node = self.helper(node.left, k)

    #     # 如果count >= k说明kth element在左子树且一定已经找到 返回一个最大值和l_node
    #     if k <= l_count: 
    #         return sys.maxsize, l_node       
    #     elif k == l_count + 1:
    #         # 出口二 node本身是kth
    #         return sys.maxsize, node
    #     else:
    #         # 继续寻找右边
    #         r_count, r_node = self.helper(node.right, k - l_count - 1)
    #         # 返回子树总结点数和r_node（没找到的情况下为空）
    #         return l_count + r_count + 1, r_node
         

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(3)
a.left = b
a.right = c
b.left = d
b.right = e
print(Solution().kthSmallest(a, 3).val)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution2:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        num_map = {}
        self.count_nodes(root, num_map)
        node = self.get_kth(root, num_map, k)
        return node.val
        
    def count_nodes(self, root, num_map):
        if root == None:
            return 0
        
        left_count = self.count_nodes(root.left, num_map)
        right_count = self.count_nodes(root.right, num_map)
        num_map[root] = left_count + right_count + 1 
        return left_count + right_count + 1 

    def get_kth(self, root, num_map, k):
        left_count = 0
        if root.left:
            left_count = num_map[root.left]
        if left_count >= k:
            return self.get_kth(root.left, num_map, k)
        elif left_count + 1 == k:
            return root
        else:
            return self.get_kth(root.right, num_map, k - 1 - left_count)
            
        