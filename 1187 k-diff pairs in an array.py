class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        if len(nums) < 2:
            return 0
            
        n = len(nums)
        
        nums.sort()
        l = 0
        r = 1 
        count = 0
        prev = None
        while l < r and r < n:
            while l < r and r < n and nums[r] - nums[l] < k:
                r += 1 
            while l < r and r < n and nums[r] - nums[l] > k:
                l += 1 
                
            if l < r and r < n and nums[r] - nums[l] == k:
                if not prev or prev != (nums[l], nums[r]):
                    count += 1 
                    prev = (nums[l], nums[r])
                r += 1
                l += 1 
        return count
            