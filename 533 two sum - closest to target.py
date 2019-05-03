import sys
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums:
            return None 
        
        nums.sort()
        
        l = 0
        r = len(nums) - 1 
        
        min_val = sys.maxsize
        while l < r:
            total = nums[l] + nums[r]
            diff = abs(total - target)
            min_val = min(diff, min_val)
            
            if total > target:
                r -= 1 
            else:
                l += 1 
        return min_val
                