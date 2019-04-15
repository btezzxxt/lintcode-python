class Solution:
    """
    @param nums: An array of integers.
    @return: nothing
    """
    def arrayReplaceWithGreatestFromRight(self, nums):
        # Write your code here.
        if not nums:
            return [] 
            
        n = len(nums)
        max_so_far = nums[-1]
        nums[-1] = -1 
        for i in range(n - 2, -1 ,-1):
            temp = nums[i]
            nums[i] = max_so_far 
            max_so_far = max(max_so_far, temp)