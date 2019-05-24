"""
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Example
Example 1

Input: 
List = [1,2,3]
k = 1
Output: 6
Explanation: 1 + 2 + 3 = 6
Example 2

Input:
List = [-1,4,-2,3,-2,3]
k = 2
Output: 8
Explanation: 4 + (3 + -2 + 3) = 8
"""

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
