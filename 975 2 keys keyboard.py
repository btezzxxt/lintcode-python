class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps(self, n):
        # Write your code here
        if n == 0 or n == 1:
            return 0
        
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i 
            for d in range(i - 1, 1, -1):
                if i % d == 0:
                    dp[i] = dp[d] + i // d 
        return dp[n]

print(Solution().minSteps(18))