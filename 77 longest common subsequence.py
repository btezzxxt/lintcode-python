class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)

        dp = [[0 for _ in range(n + 1)] for _ in range(2)]

        for i in range(n + 1):
            dp[0][i] = 0
        
        for i in range(m + 1):
            dp[i%2][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1], dp[(i-1)%2][j-1] + 1)
                else:
                    dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1])
        return dp[m%2][n]