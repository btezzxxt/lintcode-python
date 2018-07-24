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