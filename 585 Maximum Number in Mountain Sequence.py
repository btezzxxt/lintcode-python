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