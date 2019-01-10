import sys
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    # 分治法 一次去掉k的一半
    
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if not A and not B:
            return 0.0
        
        total = len(A) + len(B)
        if total % 2 == 1:
            return self.findKth(A, 0, B, 0, total // 2 + 1) * 1.0
        else:
            return self.findKth(A, 0, B, 0, total // 2 + 1) * 0.5 + self.findKth(A, 0, B, 0, total // 2) * 0.5
        
    def findKth(self, A, a_start, B, b_start, kth):
        if a_start >= len(A):
            return B[b_start + kth - 1]
        
        if b_start >= len(B):
            return A[a_start + kth - 1]

        if kth == 1:
            return min(A[a_start], B[b_start])
        
        half_kth = kth // 2
        if a_start + half_kth - 1 >= len(A):
            a_val = sys.maxsize
        else:
            a_val = A[a_start + half_kth - 1]

        if b_start + half_kth - 1 >= len(B):
            b_val = sys.maxsize
        else:
            b_val = B[b_start + half_kth - 1]
        
        if a_val < b_val:
            return self.findKth(A, a_start + half_kth, B, b_start, kth - half_kth)
        else:
            return self.findKth(A, a_start, B, b_start + half_kth, kth - half_kth)