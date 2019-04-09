import sys
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    # def findMedian(self, nums):
    #     # write your code here
    #     size = self.getTotalSize(nums)
    #     if size == 0:
    #         return 0.0
        
    #     if size % 2 == 1:
    #         return self.getKthInNums(nums, size // 2  + 1) * 1.0
    #     else:
    #         return (self.getKthInNums(nums, size // 2) + self.getKthInNums(nums, size // 2 +1)) / 2.0

    # def getKthInNums(self, nums, k):
    #     l = -sys.maxsize
    #     r = sys.maxsize
    #     for arr in nums:
    #         if not arr:
    #             continue
    #         l = min(l, arr[0])
    #         r = max(r, arr[-1])

    #     while l + 1 < r:
    #         mid = (l + r) // 2
    #         if self.numsLowerEqualToTarget(nums, mid) >= k:
    #             r = mid
    #         else:
    #             l = mid
        
    #     if self.numsLowerEqualToTarget(nums, r) >= k:
    #         return r
            
    #     if self.numsLowerEqualToTarget(nums, l) >= k:
    #         return l

    #     return 0 

    # def numsLowerEqualToTarget(self, nums, target):
    #     total = 0
    #     for arr in nums:
    #         if not arr:
    #             continue
            
    #         total += self.numsLowerEqualToTargetInArr(arr, target)
    #     return total

    # def numsLowerEqualToTargetInArr(self, arr, target):
    #     l = 0
    #     r = len(arr) - 1
    #     while l + 1 < r:
    #         mid = (l + r) // 2
    #         if arr[mid] > target:
    #             r = mid
    #         else:
    #             l = mid
        
    #     if arr[r] <= target:
    #         return r + 1
        
    #     if arr[l] <= target:
    #         return l + 1
    #     return 0

    # def getTotalSize(self, nums):
    #     if not nums:
    #         return 0
        
    #     total = 0
    #     for arr in nums:
    #         if not arr:
    #             continue
    #         total += len(arr)
    #     return total

    def findMedian(self, nums):
        n = self.count(nums)
        if n == 0:
            return 0 
        
        if n % 2 == 1:
            return self.get_kth(nums, n // 2) * 1.0
        else:
            return self.get_kth(nums, n // 2) * 0.5 + self.get_kth(nums, (n - 1)// 2 ) * 0.5

    def get_kth(self, nums, k):
        count = k + 1
        l, r = sys.maxsize, -sys.maxsize
        for arr in nums:
            if arr:
                l = min(l, arr[0])
                r = max(r, arr[-1])
        
        while l + 1 < r:
            mid = (l + r) // 2
            if self.get_total_smaller_eq(nums, mid) >= count:
                r = mid
            else:
                l = mid 
        
        if self.get_total_smaller_eq(nums, l) >= count:
            return l 
        return r 

    def get_total_smaller_eq(self, nums, val):
        total = 0 
        for num in nums:
            total += self.get_total_in_arr(num, val)
        return total

    def get_total_in_arr(self, nums, val):
        if not nums:
            return 0
        
        l = 0
        r = len(nums) - 1 
        while l + 1 < r:
            mid = (l + r) // 2 
            if nums[mid] > val:
                r = mid 
            else:
                l = mid 
        if nums[r] <= val:
            return r + 1 
        elif nums[l] <= val:
            return l + 1
        return 0
    
    def count(self, nums):
        total = 0
        for arr in nums:
            total += len(arr)
        return total 

print(Solution().findMedian([[1,3],[2147483646,2147483647]]))