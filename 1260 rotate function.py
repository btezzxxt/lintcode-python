import sys
class Solution:
    """
    @param A: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """
    def maxRotateFunction(self, A):
        # Write your code here
        n = len(A)
        f = [0] * 2 
        total = 0
        sum = 0
        for i in range(n):
            total += i * A[i]
            sum += A[i]
        f[0] = total 
        
        maxi = f[0]
        
        for i in range(1, n):
            f[i % 2] = f[(i - 1) % 2] + sum - n * A[-i]
            maxi = max(maxi, f[i % 2])
        return maxi

        