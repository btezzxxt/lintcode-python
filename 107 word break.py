class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    # dfs会超时 会超内存
    def wordBreak(self, s, dict):
        # write your code here
        if s == "":
            return True
        
        n = len(s)
        # till i can be broken
        dp = [False] * (n + 1)
        dp[0] = True 
        
        maxlen = 0
        for word in dict:
            maxlen = max(maxlen, len(word))
        
        
        for i in range(1, n + 1):
            for j in range(1, min(i, maxlen) + 1):
                if not dp[i - j]:
                    continue
                
                if s[i - j: i] in dict:
                    dp[i] = True
                    break
        return dp[n]