# from heapq import heappop, heappush
# class Solution:
#     """
#     @param nums: an integer unsorted array
#     @param k: an integer from 1 to n
#     @return: the kth largest element
#     """
#     def kthLargestElement2(self, nums, k):
#         # write your code here
#         heap = []
#         for num in nums:
#             heappush(heap, num)
#             if len(heap) > k:
#                 heappop(heap)

#         return heappop(heap)



class Solution2:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        if not nums:
            return -1
        
        return self.partition(nums, 0, len(nums) - 1, k)
        
    def partition(self, nums, start, end, k):
        if start == end:
            return nums[start]

        if start < end:
            l = start
            r = end
            
            pivot = nums[(l + r) // 2]
            while l <= r:
                while l <= r and nums[r] > pivot:
                    r -= 1 
                while l <= r and nums[l] < pivot:
                    l += 1 
            
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1 
                    r -= 1 
            if r + 1 >= k:
                return self.partition(nums, start, r, k)
            elif l + 1 <= k:
                return self.partition(nums, l, end, k)
            else:
                return nums[k]            
        
        
print(Solution2().kthLargestElement2([9,3,2,4,8],3))
      