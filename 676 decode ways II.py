class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        # write your code here
        n = len(s)
        if not s:
            return 0 
            
        dp = [0] * (n + 1)
        # dummy
        dp[0] = 1 
        if s[0] == "*":
            dp[1] = 9 
        elif s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1 
            
        for i in range(2, n + 1):
            dp[i] = (self.c2(s[i - 2], s[i - 1]) * dp[i - 2] + self.c(s[i - 1]) * dp[i - 1]) % 1000000007
        
        return dp[n]

    def c(self, char):
        if char == "*":
            return 9 
        elif char == "0":
            return 0 
        else:
            return 1
        
    def c2(self, char1, char2):
        # 11-19 21-26
        if char1 == "*" and char2 == "*":
            return 15 
        # *A A 0-6 * can be 1 or 2 --- 2 ways
        # else A can only be 1 --- 1 way
        elif char1 == "*":
            if int(char2) >= 0 and int(char2) <= 6:
                return 2 
            else:
                return 1 
        # A*
        elif char2 == "*":
            if int(char1) == 1:
                return 9 
            elif int(char1) == 2:
                return 6 
            else:
                return 0 
        # AA : 0A is not valid, out side 1-26 not valid
        else:
            if int(char1) == 0:
                return 0 
            val = int(char1 + char2)
            if val >= 1 and val <= 26:
                return 1 
            else:
                return 0
        
            
  