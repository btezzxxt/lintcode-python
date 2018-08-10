import sys
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        # dp
        # if len(nums) == 0:
        #     return 0
        # max_ = 1
        # f = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         count = 0
        #         if nums[i] > nums[j]:
        #             count = f[j] + 1
        #         f[i] = max(count, f[i])
        #     max_ = max(max_, f[i])
            
        # return max_

        # binary search minLast数组下标表示最长递增子序列的长度可能性 1-n
        # minLast数组value记录可以实现这种长度可能性下的最小结尾
        # 所以对于一个新的nums[i] 我们只需要看一看nums[i]是否大于minLast最后一个有意义的value 如果成立 下标+1 并且把这个nums[i]放在minLast的最后一个有意义位 
        def binarySearch(minLast, num):
            l = 0
            r = len(minLast) - 1
            while l + 1 < r:
                m = (l - r) // 2 + r
                if minLast[m] < num:
                    l = m
                else:
                    r = m
            return r

        minLast = [sys.maxsize] * (len(nums) + 1)
        # 第0位设置一个最小数 使得任何数都可以比它大，形成可达到长度至少为1
        minLast[0] = -sys.maxsize

        for i in range(len(nums)):
            index = binarySearch(minLast, nums[i])
            minLast[index] = nums[i]
        
        # 寻找最后一个有意义位，即可以达到的长度
        for i in range(len(nums), 0, -1):
            if minLast[i] != sys.maxsize:
                return i
        
        return 0

print(Solution().longestIncreasingSubsequence([4,2,4,5,3,7]))
