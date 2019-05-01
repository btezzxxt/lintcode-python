"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographially smallest one.

Example
Example 1

Input: 
[1,2,1,2,6,7,5,1]
2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2

Input:
[1,2,3]
1
Output: [0,1,2]
Notice
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: three non-overlapping subarrays with maximum sum
    """
    def maxSumOfThreeSubarrays(self, nums, k):
        # Write your code here
        if not nums:
            return 0 
        
        n = len(nums)
        left_maxsub_index = [] 
        right_maxsub_index = []
        sum_array = []


        total = 0
        left_max = -1
        for i in range(k):
            total += nums[i]
        left_maxsub_index.append((0, total))
        left_max = total
        sum_array.append(total)

        for i in range(k, n):
            total += nums[i]
            total -= nums[i - k]
            
            sum_array.append(total)
            if total > left_max:
                left_maxsub_index.append((i - k + 1, total))
                left_max = total
            else:
                left_maxsub_index.append(left_maxsub_index[-1])

        
        total = 0
        right_max = -1 
        for i in range(n - 1, n - k - 1, -1):
            total += nums[i]
        right_maxsub_index.append((n - k, total))
        right_max = total 

        for i in range(n - k - 1, -1, -1):
            total += nums[i]
            total -= nums[i + k]

            if total > right_max:
                right_maxsub_index.append((i, total))
                right_max = total
            else:
                right_maxsub_index.append(right_maxsub_index[-1])
        right_maxsub_index.reverse()

        total = 0
        max_val = -1
        res = []
        for i in range(k, n - 2 * k + 1):
            total = left_maxsub_index[i - k][1] + right_maxsub_index[i + k][1] + sum_array[i]
            if total > max_val:
                res = [left_maxsub_index[i - k][0], i, right_maxsub_index[i + k][0]]
                max_val = total
        return res

print(Solution().maxSumOfThreeSubarrays([4,5,10,6,11,17,4,11,1,3], 1))