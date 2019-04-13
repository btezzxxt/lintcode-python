class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0 
        
        if n == 1:
            return 1 
            
        dp = [[0 for i in range(n + 1)] for i in range(n + 1)] 
        
        for i in range(n + 1):
            dp[i][i] = 1 
                
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 
                else:
                    dp[i][j] = max(dp[i +1][j], dp[i][j - 1])

        return dp[0][n - 1]
            
            