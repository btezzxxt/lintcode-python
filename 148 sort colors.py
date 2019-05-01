"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        index = self.move_smaller_to_left(nums, 0, len(nums) - 1, 1)
        self.move_smaller_to_left(nums, index, len(nums) - 1, 2)

    def move_smaller_to_left(self, nums, start, end, pivot):
        if start < end:
            l = start
            r = end 
            while l < r:
                while l < r and nums[r] >= pivot:
                    r -= 1 
                while l < r and nums[l] < pivot:
                    l += 1 
                
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1 
                    r -= 1 
        return r
        