class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if len(A) < 3:
            return -1
        
        def shouldMoveRight(m, A):
            if A[m+1] >= A[m]:
                return True
            return False
        
        l = 0
        r = len(A) -1
        while l + 1 < r:
            m = l + (r - l) // 2
            if shouldMoveRight(m, A):
                l = m 
            else:
                r = m
        
        return l + 1 # l is the last position that should move right, so when searchends, move right 1 bit to get the peak index

# clear but timeout
import sys
class Solution2:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
    
        l = 0
        r = len(A) - 1 
        while l + 1 < r:
            m = (l + r) // 2
            if self.is_peak(A, m):
                return m
            elif self.should_search_right(A, m):
                l = m 
            else:
                r = m 
        
        if self.is_peak(A, l):
            return l
        return r
    
    def is_peak(self, A, m):
        left_value, right_value = -sys.maxsize, -sys.maxsize
        if m - 1 >= 0:
            left_value = A[m - 1]
        
        if m + 1 < len(A):
            right_value = A[m + 1]
        
        if A[m] > left_value and A[m] > right_value:
            return True
        
        return False
        
    def should_search_right(self, A, m):
        if m + 1 < len(A) and A[m + 1] > A[m]:
            return True
        return False
            