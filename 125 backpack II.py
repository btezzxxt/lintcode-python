class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        k = len(A)
        dp = [[0 for _ in range(m + 1)] for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            for j in range(0, m + 1):
                if j - A[i - 1] >= 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i -1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[k][m]
