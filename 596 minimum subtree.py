import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        min_node, min_val, cur_sum = self.findSubtreeMin(root)
        return min_node

    def findSubtreeMin(self, root):
        if root is None:
            return None, sys.maxsize, 0

        left_node, left_min, left_sum = self.findSubtreeMin(root.left)
        right_node, right_min, right_sum = self.findSubtreeMin(root.right)

        sum_ = left_sum + right_sum + root.val
        if left_min == min(left_min, right_min, sum_):
            return left_node, left_min, sum_
        if right_min == min(left_min, right_min, sum_):
            return right_node, right_min, sum_

        return root, sum_, sum_
