import sys
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0

        if not triangle[0]:
            return 0

        dp = [[sys.maxsize] * len(triangle[-1]) for i in range(2)] 
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + triangle[i][j]
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j]) + triangle[i][j]
        
        return min(dp[(len(triangle) - 1) % 2])