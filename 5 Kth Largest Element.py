# class Solution:
#     """
#     @param n: An integer
#     @param nums: An array
#     @return: the Kth largest element
#     """
#     def kthLargestElement(self, n, nums):
#         # write your code here
#         # kth biggest is len(nums) - k index smallest
#         smallest = len(nums) - n
#         return self.partition(nums, 0, len(nums) - 1, smallest)
#     # get kth smallest

#     def partition(self, nums, start, end, k):
#         if start == end:
#             return nums[k]
        
#         l, r = start, end

#         pivot = nums[(l + r)//2] 
#         while l <= r:
#             while l <= r and nums[r] > pivot:
#                 r = r - 1
#             while l <= r and nums[l] < pivot:
#                 l = l + 1
#             if l <= r:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 l = l + 1 
#                 r = r - 1
        
#         if k >= l:
#             return self.partition(nums, l, end, k)
#         elif k <= r:
#             return self.partition(nums, start, r, k) 
#         return nums[k]


from random import randint
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        
        count = len(nums)
        if count < n:
            return None
        
        return self.find_nth(nums, 0, len(nums) - 1, n)
        
        
    def find_nth(self, nums, start, end, n):
        l = start 
        r = end 
        
        rd = randint(l, r)
        nums[l], nums[rd] = nums[rd], nums[l]
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] < pivot:
                r -= 1 
            nums[l] = nums[r]
            while l < r and nums[l] > pivot:
                l += 1 
            nums[r] = nums[l]
            
        nums[l] = pivot
        index = l 
        
        if index + 1 == n:
            return nums[index]
        elif index + 1 < n:
            return self.find_nth(nums, index + 1, end, n)
        else:
            return self.find_nth(nums, start, index - 1, n)

print(Solution().kthLargestElement(3, [9, 3, 2, 4, 8]))