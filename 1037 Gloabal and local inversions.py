import sys
class Solution:
    """
    @param A: an array
    @return: is the number of global inversions is equal to the number of local inversions
    """
    def isIdealPermutation(self, A):
        # Write your code here
        if len(A) == 0 or len(A) == 1:
            return True
        
        top = -sys.maxsize
        for i in range(1, len(A)):
            if top > A[i]:
                return False 
            
            top = max(A[i - 1], top)
        return True
            