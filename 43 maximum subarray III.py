import sys
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        n = len(nums)
        if n < k:
            return 0 
        
        # dp[n][k]
        l_max = [[-sys.maxsize for i in range(k)] for i in range(n)]
        g_max = [[-sys.maxsize for i in range(k)] for i in range(n)]
        
        for i in range(n):
            if i == 0:
                l_max[0][0] = nums[i]
                g_max[0][0] = nums[i]
            else:
                l_max[i][0] = max(l_max[i - 1][0] + nums[i], nums[i])
                g_max[i][0] = max(g_max[i - 1][0], l_max[i][0])
        
        for j in range(1, k):
            for i in range(j, n):
                l_max[i][j] = max(l_max[i - 1][j] + nums[i], g_max[i - 1][j - 1] + nums[i])
                g_max[i][j] = max(l_max[i][j], g_max[i - 1][j])
                
        return g_max[n - 1][k - 1]