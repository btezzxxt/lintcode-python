class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if n == 0:
            return 0
        
        f = [0] * n 
        if n == 1:
            return k
        
        f[0] = k 
        f[1] = f[0] * k
                
        
        for i in range(2, n):
            f[i] = (k - 1) * f[i - 1] + (k - 1) * f[i - 2]
        return f[-1]