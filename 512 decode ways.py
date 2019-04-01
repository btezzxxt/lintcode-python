class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    # dps 超时
    def numDecodings(self, s):
        # write your code here
        if s == "":
            return 0
        
        valid, count = self.dfs(s, 0)
        if valid:
            return count
        return 0
        
    def dfs(self, s, start):
        if start == len(s):
            return True, 1
            
        first_num = int(s[start])
        if first_num == 0:
            return False, 0
        
        if start + 1 < len(s):
            second_num = int(s[start + 1])
            if (first_num == 1 or first_num == 2) and second_num == 0:
                return self.dfs(s, start + 2)
            elif first_num == 1 or (first_num == 2 and second_num > 0 and second_num <= 6):
                valid1, count1 = self.dfs(s, start + 1)
                valid2, count2 = self.dfs(s, start + 2)
                if valid1 and valid2:
                    return True, count1 + count2
                elif valid1:
                    return True, count1
                elif valid2:
                    return True, count2
                else:
                    return False, 0
                
        return self.dfs(s, start + 1)

print(Solution().numDecodings("8901"))

class Solution2:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    # dp, on time
    # 用dp[i] 记录1-i个数的decode方法
    # 值得注意的地方是初始化了dp[1] = 1; dp[0] = 1 作为一个dummy点； ep: 12； dp[1] 为1 的decode方法； dp[2] = dp[1] + dp[0]刚好两个点
    def numDecodings(self, s):
        # write your code here
        if len(s) == 0:
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        
        if int(s[0]) == 0:
            return 0 
        # this is the boundary, dummy head, doens't mean anything
        dp[0] = 1
        # if the first char is not 0, we have one valid decode        
        dp[1] = 1
        
        for i in range(2, n + 1):
            pre = int(s[i - 2])
            cur = int(s[i - 1])
            # 10, 20
            if (pre == 1 or pre == 2) and cur == 0:
                dp[i] = dp[i - 2]
            # 11-19 21-26, two possible decodes
            elif (pre == 1) or (pre == 2 and cur <= 6):
                dp[i] = dp[i - 2] + dp[i - 1]
            # 30 40 50 - 90 is not valid, return 0 directly
            elif (pre != 1 and pre != 2) and cur == 0:
                return 0
            else:
                dp[i] = dp[i - 1]
        return dp[n]
        
        