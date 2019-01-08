import sys
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        # prefix sum算法
        maxGap = -sys.maxsize
        minSum = sys.maxsize
        sum = 0
        for num in nums:
            sum += num
            maxGap = max(maxGap, sum - minSum)
            minSum = min(minSum, sum)

        return maxGap

        # 状态转移方程 以i为结尾的subarray最大值，f(i-1) + nums[i] or just nums[i] 取较大者  

        #DP
        # if len(nums) == 0:
        #     return 0
            
        # if len(nums) == 1:
        #     return nums[0]
        
        # len_ = len(nums)
        # f = [-sys.maxsize] * 2

        # max_ = -sys.maxsize

        # for i in range(0, len_):
        #     if i == 0:
        #         f[i % 2] = nums[0]
        #     else:
        #         f[i % 2] = max(f[(i - 1) % 2] + nums[i], nums[i])
        #     max_ = max(max_, f[i % 2])
        
        # return max_