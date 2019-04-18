import sys
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs or not costs[0]:
            return 0 
        
        n = len(costs)
        k = len(costs[0])
        
        dp = [[0 for i in range(k)] for i in range(n + 1)]
        
        for i in range(1, n + 1):
            # reset min1, min2 every round
            min1, min2, id1, id2 = sys.maxsize, sys.maxsize, 0, 0
            for j in range(k):
                if dp[i - 1][j] < min1:
                    min2 = min1
                    id2 = id1
                    min1 = dp[i - 1][j]
                    id1 = j
                else:
                    if dp[i - 1][j] < min2:
                        min2, id2 = dp[i - 1][j], j
            
            for j in range(k):
                if j == id1:
                    dp[i][j] = costs[i - 1][j] + min2
                else:
                    dp[i][j] = costs[i - 1][j] + min1
        return min(dp[n])