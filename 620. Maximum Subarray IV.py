import sys
class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        # write your code here
        if not nums:
            return 0 
            
        n = len(nums)
        if n < k:
            return 0
        
        
        sum_arr = [0] * (n + 1)
        min_sum_arr = [0] * (n + 1)
        
        
        for i in range(1, n + 1):
            sum_arr[i] = sum_arr[i - 1] + nums[i - 1]
            min_sum_arr[i] = min(min_sum_arr[i - 1], sum_arr[i])
        
        max_val = -sys.maxsize
        for i in range(k, n + 1):
            max_val = max(max_val, sum_arr[i] - min_sum_arr[i - k])
        return max_val
                
        