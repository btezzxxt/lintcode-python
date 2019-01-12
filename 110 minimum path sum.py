import sys

# 空间复杂度使用%降维
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if len(grid) == 0:
            return 0
        
        if len(grid[0]) == 0:
            return 0

        dp = [[0] * len(grid[0]) for i in range(2)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue

                pre_left, pre_top = sys.maxsize, sys.maxsize
                if j - 1 >= 0:
                    pre_left = dp[i % 2][j - 1]
                
                if i - 1 >= 0:
                    pre_top = dp[(i - 1) % 2][j]
                    
                dp[i % 2][j] = min(pre_left + grid[i][j], pre_top + grid[i][j])
        return dp[(len(grid) - 1) % 2][-1]


print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))