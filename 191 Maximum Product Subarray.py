import sys
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        
        F = 2 * [0]
        G = 2 * [0]
        F[0] = nums[0]
        G[0] = nums[0]
        max_ = max(-sys.maxsize, F[0])
            
        for i in range(1, len(nums)):
            F[i % 2] = max(F[(i-1) % 2] * nums[i], nums[i], G[(i-1) % 2] * nums[i])
            G[i % 2] = min(F[(i-1) % 2] * nums[i], nums[i], G[(i-1) % 2] * nums[i])
            max_ = max(max_, F[i % 2])
            
        return max_