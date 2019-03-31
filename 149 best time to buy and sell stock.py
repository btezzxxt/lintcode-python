class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
        
        # always remember the lowest price so far 
        # use a global variable to rememeber max_profit so far
        minval = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i]
            profit = max(profit, p - minval)
            if p < minval:
                minval = p 
        return profit
        