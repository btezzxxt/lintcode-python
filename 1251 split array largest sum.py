import sys
class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        # write your code here
        total = sum(nums)
        l = 0
        r = total
        while l + 1 < r:
            mid = (l + r) // 2 
            if self.split_array_nums(mid, nums) <= m:
                r = mid 
            else:
                l = mid 
        
        if self.split_array_nums(l, nums) == m:
            return l 
        else:
            return r 
    
    def split_array_nums(self, cap, nums):
        count = 1
        cur = 0
        for num in nums:
            if num > cap:
                return sys.maxsize

            if cur + num <= cap:
                cur += num 
            else:
                cur = num 
                count += 1 
        return count
        
print(Solution().splitArray([1, 4, 4], 3))