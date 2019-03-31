# class Solution:
#     """
#     @param prices: Given an integer array
#     @return: Maximum profit
#     """
#     def maxProfit(self, prices):
#         # write your code here
#         if not prices or len(prices) == 1:
#             return 0
            
#         total = 0        
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 total += prices[i] - prices[i - 1]
#         return total

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
        
        # dp 做法 dp[i] 表示到i结尾的部分最大profit
        dp = [0 for i in range(2)] 
        dp[0] = 0
        low = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - low
            dp[i % 2] = max(dp[(i - 1) % 2], profit)
            if prices[i] < low:
                low = prices[i]
                
        return dp[(len(prices) - 1) % 2]


class Solution2:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    # 比较取巧的一种解法，用一个dp记录从0 到i的max profit
    # 再用另一个dp记录从右往左 n -1到i的max profit
    # 然后对每一组0-i-n-1进行查询 找到最大
    def maxProfit(self, prices):
        # write your code here
        # tricky two way single buy dp:
        if not prices or len(prices) == 1:
            return 0
            
        n = len(prices)
        # dp from the left, ldp[i] means from 0 to i, max profit
        ldp = [0 for i in range(n)]
        ldp[0] = 0
        min_val = prices[0]
        for i in range(1, n):
            ldp[i] = max(ldp[i - 1], prices[i] - min_val)
            min_val = min(min_val, prices[i])
        
        #dp from the right, from n -1 to i, max profit
        rdp = [0 for i in range(n)]
        max_val = prices[n - 1]
        rdp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            rdp[i] = max(rdp[i + 1], max_val - prices[i])
            max_val = max(max_val, prices[i])
        
        profit = 0
        for i in range(n):
            profit = max(profit, ldp[i] + rdp[i])
        return profit