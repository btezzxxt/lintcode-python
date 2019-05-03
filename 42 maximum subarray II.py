"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

Example
Example 1:

Input:
[1, 3, -1, 2, -1, 2]
Output:
7
Explanation:
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
Example 2:

Input:
[5,4]
Output:
9
Explanation:
the two subarrays are [5] and [4].
Challenge
Can you do it in time complexity O(n) ?
"""

import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0
        
        n = len(nums)

        local = nums[0]
        global_max = nums[0]
        left_max_sum = [nums[0]]
        for i in range(1, n):
            local += nums[i]
            local = max(local, nums[i])
            global_max = max(local, global_max)
            left_max_sum.append(global_max)

        local = nums[-1]
        global_max = nums[-1]
        right_max_sum = [nums[-1]]
        for i in range(n - 2, -1, -1):
            local += nums[i]
            local = max(local, nums[i])
            global_max = max(local, global_max)
            right_max_sum.append(global_max)
        right_max_sum.reverse()

        max_val = -sys.maxsize
        for i in range(1, n):
            max_val = max(max_val, (left_max_sum[i - 1] + right_max_sum[i]))
        return max_val



print(Solution().maxTwoSubArrays([1, 3, -1, 2, -1, 2]))