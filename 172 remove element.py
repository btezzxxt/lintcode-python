class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        if not A:
            return 0
        
        l = 0 
        r = len(A) - 1 
        while l < r:
            while l < r and A[r] == elem:
                r -= 1 
            
            while l < r and A[l] != elem:
                l += 1 
            
            if l < r:
                A[l], A[r] = A[r], A[l]
                l += 1 
                r -= 1

        while l < len(A):
            if A[l] == elem:
                break 
            l += 1

        return l