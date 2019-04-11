# import sys
# class Solution:
#     """
#     @param: A: An integer array
#     @param: B: An integer array
#     @return: a double whose format is *.5 or *.0
#     """
#     # 分治法 一次去掉k的一半
    
#     def findMedianSortedArrays(self, A, B):
#         # write your code here
#         if not A and not B:
#             return 0.0
        
#         total = len(A) + len(B)
#         if total % 2 == 1:
#             return self.findKth(A, 0, B, 0, total // 2 + 1) * 1.0
#         else:
#             return self.findKth(A, 0, B, 0, total // 2 + 1) * 0.5 + self.findKth(A, 0, B, 0, total // 2) * 0.5
        
#     def findKth(self, A, a_start, B, b_start, kth):
#         if a_start >= len(A):
#             return B[b_start + kth - 1]
        
#         if b_start >= len(B):
#             return A[a_start + kth - 1]

#         if kth == 1:
#             return min(A[a_start], B[b_start])
        
#         half_kth = kth // 2
#         if a_start + half_kth - 1 >= len(A):
#             a_val = sys.maxsize
#         else:
#             a_val = A[a_start + half_kth - 1]

#         if b_start + half_kth - 1 >= len(B):
#             b_val = sys.maxsize
#         else:
#             b_val = B[b_start + half_kth - 1]
        
#         if a_val < b_val:
#             return self.findKth(A, a_start + half_kth, B, b_start, kth - half_kth)
#         else:
#             return self.findKth(A, a_start, B, b_start + half_kth, kth - half_kth)

import sys
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """    
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n == 0:
            return 0
        
        if n % 2 == 1:
            return self.find_kth([A, B], n // 2)
        else:
            return self.find_kth([A, B], n // 2) * 0.5 + self.find_kth([A, B], (n - 1) // 2) * 0.5
        
    def find_kth(self, nums, k):
        count = k + 1 
        l, r = sys.maxsize, -sys.maxsize
        for num in nums:
            if num:
                l = min(l, num[0])
                r = max(r, num[-1])

        while l + 1 < r:
            mid_val = (l + r) // 2
            if self.get_smaller_eq(nums, mid_val) >= count:
                r = mid_val
            else:
                l = mid_val 
        
        if self.get_smaller_eq(nums, l) >= count:
            return l 
        else:
            return r 

    def get_smaller_eq(self, nums, val):
        total = 0 
        for num in nums:
            total += self.get_smaller_eq_in_arr(num, val)
        return total 
    
    def get_smaller_eq_in_arr(self, num, val):
        if not num:
            return 0

        l = 0
        r = len(num) - 1 
        while l + 1 < r:
            mid_index = (l + r) // 2
            if num[mid_index] > val:
                r = mid_index 
            else:
                l = mid_index 

        if num[r] <= val:
            return r + 1
        if num[l] <= val:
            return l + 1 
        return 0

print(Solution().findMedianSortedArrays([1,3,9,10], [1,4,6,6,10,11]))

        
        