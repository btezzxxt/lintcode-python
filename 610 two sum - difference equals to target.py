class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        map = {}
        
        for i in range(1, len(nums) + 1):
            index = i - 1 
            num = nums[index]
            
            if num in map:
                return [map[num], i]
            
            map[num - target] = i 
            map[num + target] = i 
        return []
            
        
