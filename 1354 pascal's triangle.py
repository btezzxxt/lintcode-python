class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def getRow(self, rowIndex):
        # write your code here
        if rowIndex < 1:
            return [] 
            
        dp = [[0 for i in range(rowIndex + 1)] for i in range(2)]
        dp[0][0] = 1 
        for i in range(1, rowIndex + 1):
            for j in range(0, rowIndex + 1):
                if j == 0:
                    dp[i%2][j] = 1
                else:
                    dp[i%2][j] = dp[(i - 1)%2][j - 1] + dp[(i - 1)%2][j]
        
        return dp[rowIndex%2]
                    
                
