class Solution:
    """
    @param nums: an array
    @return: the corresponding expression in string format
    """
    def optimalDivision(self, nums):
        # Write your code here
        if not nums:
            return ""
        
        if len(nums) == 1:
            return str(nums[0])
            
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        
        res = [str(nums[0])]
        for i in range(1, len(nums)):
            if i == 1:
                res.append("/(")
                res.append(str(nums[i]))
            else:
                res.append("/")
                res.append(str(nums[i]))
        res.append(")")
        return "".join(res)