class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    def nextGreaterElements(self, nums):
        # Write your code here
        if not nums:
            return nums
        stack = []
        n = len(nums)
        
        res = [-1] * n
        nums.extend(nums)
        
        for index, num in enumerate(nums):
            if stack:
                while stack and stack[-1][0] < num:
                    top = stack.pop()
                    res[top[1] % n] = num
            stack.append((num, index))
        return res            
        
                
            
        
        
