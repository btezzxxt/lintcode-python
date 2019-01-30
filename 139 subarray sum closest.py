import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            cur_sum = (prefix_sum[-1][0] + num, i)
            prefix_sum.append(cur_sum)
        
        prefix_sum.sort()

        mini = sys.maxsize 
        for i in range(1, len(prefix_sum)):
            diff = prefix_sum[i][0] - prefix_sum[i-1][0]
            if diff < mini:
                mini = diff
                left = min(prefix_sum[i][1], prefix_sum[i-1][1]) + 1
                right = max(prefix_sum[i][1], prefix_sum[i-1][1])
        
        return [left, right]


print(Solution().subarraySumClosest([-3,1,1,-3,5]))