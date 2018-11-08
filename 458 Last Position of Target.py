class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                l = m
            elif nums[m] < target:
                l = m
            else:
                r = m
        
        if nums[r] == target:
            return r
        
        if nums[l] == target:
            return l
        
        return -1

print(Solution().lastPosition([1,2,2,4,5,5], 2))