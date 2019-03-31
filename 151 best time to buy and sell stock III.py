# O(n2)的搜索方案， 会超时
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
            
        profit = 0
        for i in range(len(prices)):
            profit_left = self.one_trans_profix(prices, 0, i)
            profit_right = self.one_trans_profix(prices, i + 1, len(prices) - 1)
            profit = max(profit, profit_left + profit_right)
        return profit
        
    
    def one_trans_profix(self, prices, start, end):
        if start >= end:
            return 0
        
        low = prices[start]
        profit = 0
        for i in range(start + 1, end + 1):
            profit = max(prices[i] - low, profit)
            if prices[i] < low:
                low = prices[i]
        return profit