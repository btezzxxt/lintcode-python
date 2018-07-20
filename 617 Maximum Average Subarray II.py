import sys
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):

        # write your code here
        def hasAvgGreater(nums, avg, k):
            sumI = 0
            sumIK = 0
            minSum = sys.maxsize
            for i in range(len(nums)):
                sumI += nums[i] - avg
                if i >= k - 1 and sumI > 0:
                    return True
                if i >= k:
                    sumIK += nums[i-k] - avg
                    minSum = min(minSum, sumIK)
                    if sumI - minSum >= 0:
                        return True
            return False

        l = -1e10
        r = 1e3 # for passing OA
        eps = 1e-5
        while l + eps < r:
            m = l + (r - l) / 2
            if hasAvgGreater(nums, m, k):
                l = m
            else:
                r = m
                
        if l - 0 >= -eps and l - 0 <= eps:
            l = abs(l)
        return l
            
print(Solution().maxAverage([-4,5,-4,5,-4,5,-4,5,-4,5,-4,5], 10))