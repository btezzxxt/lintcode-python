import sys
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        i = 0
        j = 0
        sum = 0
        mincount = sys.maxsize
        while j < len(nums):
            sum += nums[j]
            while sum >= s:
                mincount = min(j - i + 1, mincount)
                sum -= nums[i]
                i += 1
            j += 1
        
        return mincount if mincount != sys.maxsize else -1

print(Solution().minimumSize([2,3,1,2,4,3], 7))




            