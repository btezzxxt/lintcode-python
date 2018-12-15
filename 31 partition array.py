class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0:
            return 0

        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[r] >= k:
                r = r - 1
            while l < r and nums[l] < k:
                l = l + 1                
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        # a few ending cases eg: k = 5
        # case 1 [4, 4, 4] l is in the end index, should return l + 1
        # case 2 [6, 6, 6] l is at 0 index, should return l since nums[l] >= k 
        # case 3 [4, 5, 6] l is at 4 (0 index) should return l + 1
        # to sum up: 
        if nums[l] >= k:
            return l 
        else:
            return l + 1
