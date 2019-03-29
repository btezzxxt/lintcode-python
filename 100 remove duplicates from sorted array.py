class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
            
        size = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[size]:
                size += 1 
                nums[size] = nums[i]
        return size + 1 
        
# p1 + 1 的时机很关键