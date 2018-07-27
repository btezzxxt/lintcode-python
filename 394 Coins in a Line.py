class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        
        if n < 3:
            return True
            
        f = [False] * 3
        
        f[0] = True
        f[1] = True
        for i in range(2, n):
            f[i % 3] = not (f[(i-1) % 3] and f[(i-2) % 3])

        return f[(n-1) % 3]