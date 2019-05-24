import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0 
        
        n = len(nums)
        left_sum_arr = [None] * n 
        right_sum_arr = [None] * n 

        global_max = -sys.maxsize
        global_min = sys.maxsize
        local_max = 0
        local_min = 0
        for i, num in enumerate(nums):
            local_max += num 
            local_max = max(local_max, num)
            global_max = max(global_max, local_max)

            local_min += num 
            local_min = min(local_min, num)
            global_min = min(global_min, local_min)

            left_sum_arr[i] = (global_max, global_min)

        global_max = -sys.maxsize
        global_min = sys.maxsize
        local_max = 0
        local_min = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            local_max += num 
            local_max = max(local_max, num)
            global_max = max(local_max, global_max)

            local_min += num 
            local_min = min(local_min, num)
            global_min = min(local_min, global_min)         

            right_sum_arr[i] = (global_max, global_min)     

        max_val = -sys.maxsize
        for i in range(1, n):
            left_max, left_min = left_sum_arr[i - 1]
            right_max, right_min = right_sum_arr[i]
            max_val = max(max_val, abs(left_max - right_min), abs(left_min - right_max))
        return max_val

print(Solution().maxDiffSubArrays([-5, -4]))