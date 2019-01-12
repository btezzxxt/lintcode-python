class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        
        dp = [0] * 3
        for i in range(n):
            if i == 0:
                dp[i] = 1
                continue
            
            if i == 1:
                dp[i] = 2
                continue
            
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]

        return dp[(n - 1) % 3]
            
