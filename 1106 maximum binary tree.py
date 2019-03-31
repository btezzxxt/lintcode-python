class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, start, end):
        if start > end:
            return None
        
        maxi = nums[start]
        index = start
        for i in range(start, end + 1):
            if nums[i] > maxi:
                maxi = nums[i]
                index = i
        node = TreeNode(maxi)
        node.left = self.helper(nums, start, index - 1)
        node.right = self.helper(nums, index + 1, end)
        return node