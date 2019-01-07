import sys
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        size = self.getTotalSize(nums)
        if size == 0:
            return 0.0
        
        if size % 2 == 1:
            return self.getKthInNums(nums, size // 2  + 1) * 1.0
        else:
            return (self.getKthInNums(nums, size // 2) + self.getKthInNums(nums, size // 2 +1)) / 2.0

    def getKthInNums(self, nums, k):
        l = -sys.maxsize
        r = sys.maxsize
        for arr in nums:
            if not arr:
                continue
            l = min(l, arr[0])
            r = max(r, arr[-1])

        while l + 1 < r:
            mid = (l + r) // 2
            if self.numsLowerEqualToTarget(nums, mid) >= k:
                r = mid
            else:
                l = mid
        
        if self.numsLowerEqualToTarget(nums, r) >= k:
            return r
            
        if self.numsLowerEqualToTarget(nums, l) >= k:
            return l

        return 0 

    def numsLowerEqualToTarget(self, nums, target):
        total = 0
        for arr in nums:
            if not arr:
                continue
            
            total += self.numsLowerEqualToTargetInArr(arr, target)
        return total

    def numsLowerEqualToTargetInArr(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid] > target:
                r = mid
            else:
                l = mid
        
        if arr[r] <= target:
            return r + 1
        
        if arr[l] <= target:
            return l + 1
        return 0

    def getTotalSize(self, nums):
        if not nums:
            return 0
        
        total = 0
        for arr in nums:
            if not arr:
                continue
            total += len(arr)
        return total