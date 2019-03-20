class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        def isPeak(index):
            len_ = len(nums)
            
            leftValue = -1
            if index - 1 >= 0 and index - 1 < len_:
                leftValue = nums[index - 1]
        
            rightValue = -1
            if index + 1 >= 0 and index + 1 < len_:
                rightValue = nums[index + 1]
                
            if nums[index] > leftValue and nums[index] > rightValue:
                return True
            
            return False
            
        def peakOnRight(index):
            len_ = len(nums)

            rightValue = -1
            if index + 1 >= 0 and index + 1 < len_:
                rightValue = nums[index + 1]
                
            if nums[index] < rightValue:
                return True
            
            return False    
                
        # write your code here
        l = 0
        r = len(nums)
        while l + 1 < r:
            m = l + (r - l) // 2
            if isPeak(m) or peakOnRight(m):
                l = m 
            else:
                r = m 
        
        if isPeak(l):
            return nums[l]
        
        if isPeak(r):
            return nums[r]
        
        return -1

print(Solution().mountainSequence([10,9,8,7]))

class Solution2:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        if not nums:
            return -1 
        
        l = 0
        r = len(nums) - 1 
        while l + 1 < r:
            m = (l + r) // 2
            if self.is_peak(nums, m):
                return nums[m]
            elif self.peak_on_right(nums, m):
                l = m 
            else:
                r = m 
        
        if self.is_peak(nums, r):
            return nums[r]
        
        if self.is_peak(nums, l):
            return nums[l]
        
        return -1
    
    def is_peak(self, nums, index):
        left_smaller, right_smaller = False, False
        if (index - 1 >= 0 and nums[index - 1] < nums[index]) or index - 1 < 0:
            left_smaller = True
        
        if (index + 1 < len(nums) and nums[index + 1] < nums[index]) or index + 1 >= len(nums):
            right_smaller = True
        
        return left_smaller and right_smaller
    
    def peak_on_right(self, nums, index):    
        if index + 1 < len(nums) and nums[index + 1] > nums[index]:
            return True
        return False