class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if len(s) == 0:
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        
        # this is the boundary, dummy head, doens't mean anything
        dp[0] = 1
        # if the first char is not 0, we have one valid decode        
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = self.ways(s[i - 1]) * dp[i - 1] + self.ways2(s[i - 2], s[i - 1]) * dp[i - 2]
        return dp[n]
            
            
            
    def ways(self, char):
        if char == "0":
            return 0 
        else:
            return 1 
    
    def ways2(self, char1, char2):
        if char1 == "0":
            return 0 
        
        val = int(char1 + char2)
        if val >= 1 and val <= 26:
            return 1 
        return 0        
            