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