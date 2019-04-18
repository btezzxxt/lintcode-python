class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs or not costs[0]:
            return 0
        
        # min cost of ith house to be red, blue, or green
        n = len(costs)
        red = [0] * n 
        blue = [0] * n 
        green = [0] * n 
        
        red[0] = costs[0][0]
        blue[0] = costs[0][1]
        green[0] = costs[0][2]
        
        for i in range(1, n):
            red[i] = costs[i][0] + min(blue[i - 1], green[i - 1])
            blue[i] = costs[i][1] + min(red[i - 1], green[i - 1])
            green[i] = costs[i][2] + min(red[i - 1], blue[i - 1])
        
        return min(red[n - 1], blue[n - 1], green[n - 1])