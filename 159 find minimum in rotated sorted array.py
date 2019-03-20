# https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description?_from=ladder&&fromId=1
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        token = nums[-1]
        left = 0 
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left - right) // 2 + right
            if nums[mid] < token:
                right = mid
            else:
                left = mid 
        
        if nums[right] > token and right + 1 < len(nums):
            return nums[right + 1]
        elif nums[left] > token and left + 1 < len(nums):
            return nums[left + 1]
        else:
            return nums[0]

# https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description?_from=ladder&&fromId=1
class Solution2:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if len(nums) == 0:
            return
        
        pivot = nums[0]
        
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if self.is_minimal(nums, m):
                return nums[m]
            elif self.should_move_right(nums, m, pivot):
                l = m 
            else:
                r = m 
        
        print(l, r)
        if self.is_minimal(nums, l):
            return nums[l]
        
        if self.is_minimal(nums, r):
            return nums[r]
            
        return pivot
            
    def is_minimal(self, nums, index):
        if index - 1 >= 0 and nums[index - 1] > nums[index]:
            return True
        return False
    
    def should_move_right(self, nums, index, pivot):
        if nums[index] > pivot:
            return True
        return False
        