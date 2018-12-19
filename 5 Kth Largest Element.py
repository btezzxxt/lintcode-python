class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # kth biggest is len(nums) - k smallest + 1
        smallest = len(nums) - n + 1
        return self.partition(nums, 0, len(nums) - 1, smallest)
    # get kth smallest
    def partition(self, nums, l, r, k):
        if l == r:
            return nums[k - 1]
        
        pivot = nums[(l + r) // 2] 
        while l <= r:

            while l <= r and nums[l] < pivot:
                l = l + 1
            while l <= r and nums[r] > pivot:
                r = r - 1                
            if l <= r:
                nums[r], nums[l] = nums[l], nums[r]
                l = l + 1
                r = r - 1

        if k -1<= r:
            return self.partition(nums, 0, r, k) 
        if k -1 >= l:
            return self.partition(nums, l, len(nums) - 1, k)

        return nums[k - 1]

# class Solution:
#     # @param k & A a integer and an array
#     # @return ans a integer
#     def kthLargestElement(self, k, A):
#         if not A or k < 1 or k > len(A):
#             return None
#         return self.partition(A, 0, len(A) - 1, len(A) - k)
        
#     def partition(self, nums, start, end, k):
#         """
#         During the process, it's guaranteed start <= k <= end
#         """
#         if start == end:
#             return nums[k]
            
#         left, right = start, end
#         pivot = nums[(start + end) // 2]
#         while left <= right:
#             while left <= right and nums[left] < pivot:
#                 left += 1
#             while left <= right and nums[right] > pivot:
#                 right -= 1
#             if left <= right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left, right = left + 1, right - 1
                
#         # left is not bigger than right
#         if k <= right:
#             return self.partition(nums, start, right, k)
#         if k >= left:
#             return self.partition(nums, left, end, k)
        
#         return nums[k]

print(Solution().kthLargestElement(3, [9,3,2,4,8]))