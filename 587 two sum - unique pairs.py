class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        
        l = 0
        r = len(nums) - 1 

        count = 0        
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                count += 1 
                l += 1 
                while l < r and nums[l] == nums[l - 1]:
                    l += 1 
                
                r -= 1 
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1 
            elif total > target:
                r -= 1 
            else:
                l += 1 
        return count 
        
        