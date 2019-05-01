"""
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example
Example1

Input:  nums = [3,6,4]
Output: 6
Example2

Input:  nums = [2,3,2,3]
Output: 6
"""
class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        max_val1 = self.houseRobber(nums, 1, len(nums) - 1)
        max_val2 = self.houseRobber(nums, 0, len(nums) - 2)
        return max(max_val1, max_val2)

    def houseRobber(self, nums, start, end):
        dp = [0] * (len(nums) + 1)

        if start == end:
            return nums[start]

        dp[start] = nums[start]
        dp[start + 1] = max(dp[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return max(dp[end], dp[end - 1])