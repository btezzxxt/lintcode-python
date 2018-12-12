class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return []
        
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] + nums[r] < target:
                l = l + 1
            while l < r and nums[l] + nums[r] > target:
                r = r - 1
            
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]

        return []