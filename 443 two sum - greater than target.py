class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums:
            return 0
        
        nums.sort()
        l = 0
        r = len(nums) - 1 
        count = 0
        while l < r:
            total = nums[l] + nums[r]
            if total <= target:
                l += 1 
            else:
                count += r - l 
                r -= 1 
        return count
