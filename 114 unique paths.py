class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == 0:
            return 0
        
        if n == 0:
            return 0

        dp = [[0] * n for i in range(2)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                
                path_left, path_top = 0, 0
                if j - 1 >= 0:
                    path_left = dp[i % 2][j - 1]
                if i - 1 >= 0:
                    path_top = dp[(i - 1) % 2][j]
                
                dp[i % 2][j] = path_left + path_top
        
        return dp[(m - 1) % 2][n - 1]

print(Solution().uniquePaths(1, 3))