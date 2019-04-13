import sys
class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        # Write your code here
        n = len(A)
        keep = [sys.maxsize] * (n + 1)
        swap = [sys.maxsize] * (n + 1)
        
        keep[0] = 0        
        swap[0] = 1
        
        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1 
            
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(keep[n - 1], swap[n - 1])