import sys
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        act = K * 2
        if act >= len(prices):
            return self.quick_count(prices)
            
        n = len(prices)
        rest = [[0] * n for i in range(act + 1)]
        hold = [[-sys.maxsize] * n for i in range(act + 1)]

        for i in range(1, act + 1):
            hold[i][0] = -prices[0]
        
        for i in range(1, act + 1):
            for j in range(1, n):
                rest[i][j] = max(rest[i][j - 1], hold[i - 1][j - 1] + prices[j])
                hold[i][j] = max(hold[i][j - 1], rest[i - 1][j - 1] - prices[j])
        return rest[act][n - 1]
            
    def quick_count(self, prices):
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]
        return total

print(Solution().maxProfit(2,[3,3,5,0,0,3,1,4]))