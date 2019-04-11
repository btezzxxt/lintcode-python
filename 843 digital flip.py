class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        # Write your code here
        n = len(nums)
        i_is_zero = [0] * n 
        i_is_one = [0] * n 
        
        if nums[-1] == 1:
            i_is_zero[-1] = 1 
            i_is_one[-1] = 0
        else:
            i_is_zero[-1] = 0
            i_is_one[-1] = 1 
            
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                i_is_one[i] = 1 + min(i_is_zero[i + 1], i_is_one[i + 1])
                i_is_zero[i] = i_is_zero[i + 1]
            else:
                i_is_one[i] = min(i_is_zero[i + 1], i_is_one[i + 1])
                i_is_zero[i] = 1 + i_is_zero[i + 1]
        return min(i_is_zero[0], i_is_one[0])
                