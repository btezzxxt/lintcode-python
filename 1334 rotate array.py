class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        if not nums:
            return nums
        
        n = len(nums)
        if k > n:
            k %= n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        return nums 
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1 
            end -= 1 

            
