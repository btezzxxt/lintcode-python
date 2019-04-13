class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        if not nums:
            return []
        
        n = len(nums)
        
        res = []
        for i in range(n):
            if nums[i] == i + 1:
                continue
            
            val = nums[i]
            while 1:
                val_idx = val - 1
                if val_idx == i:
                    nums[val_idx] = val
                    break
                
                if nums[val_idx] == val:
                    if not res:
                        res.append(val)
                    break
                nums[val_idx], val = val, nums[val_idx]
        
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
                
        return res
        