class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        a = 1
        minNode, minVal, curSum = self.findSubtreeMinfindSubtreeMin(root)
        return minNode
    
    def findSubtreeMin(self, root):
        if root == None:
            return None, 0, 0

        leftNode, leftMin, leftsum = self.findSubtreeMin(root.left)
        rightNode, rightMin, rightSum = self.findSubtreeMin(root.right)

        sum_ = leftSum + rightSum + root.val
        if leftMin = min(leftMin, rightMin, sum_):
            return leftNode, leftMin, sum_ 
        if rightMin = min(leftMin, rightMin, sum_):
            return rightNode, rightMin, sum_

        return root, sum_, sum_

print(Solution().findSubtree(1))