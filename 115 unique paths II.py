class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid:
            return 0
        
        if not obstacleGrid[0]:
             return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for i in range(2)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i % 2][j] = 0
                    continue
                
                if i == 0 and j == 0:
                    dp[i % 2][j] = 1
                    continue
                
                left_path, top_path = 0, 0
                if i - 1 >= 0:
                    top_path = dp[(i - 1) % 2][j]
                
                if j - 1 >= 0:
                    left_path = dp[i % 2][j - 1]
                
                dp[i % 2][j] = top_path + left_path
        
        return dp[(m - 1) % 2][n - 1]

print(Solution().uniquePathsWithObstacles([[0,0],[0,0],[0,0],[1,0],[0,0]]))