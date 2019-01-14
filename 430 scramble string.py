class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    # 记忆化搜索
    def isScramble(self, s1, s2):
        # write your code here
        return self.helper(s1, s2, {})

    def helper(self, s1, s2, visited):
        if (s1, s2) in visited:
            return visited[(s1, s2)]

        if len(s1) != len(s2):
            return False
        
        if len(s1) == 1:
            return s1 == s2
        
        n = len(s1)
        for k in range(1, len(s1)):
            # s1前k个数匹配了s2前k个数， 后n-k个数匹配了后n-k个数
            case1 = self.helper(s1[: k], s2[: k], visited) and self.helper(s1[k:], s2[k:], visited)
            
            # 或者前k个数[0:k]匹配了后k个数[n-k:n],后n-k个数匹配s2前k个数
            case2 = self.helper(s1[: k], s2[n - k:], visited) and self.helper(s1[k:], s2[: n - k], visited)
            is_scramble = case1 or case2
            if is_scramble:
                visited[(s1, s2)] = True
                return True
        
        visited[(s1, s2)] = False
        return False

print(Solution().isScramble("abb", "bba"))