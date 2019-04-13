class Solution:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeatedSubstringPattern(self, s):
        return s in (s+s)[1: -1]

class Solution2:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeatedSubstringPattern(self, s):
        # write your code here
        if s == "":
            return True
        
        for i in range(1, len(s)):
            pattern = s[:i]
            if self.dfs(s, 0, pattern):
                return True
        return False
    
    def dfs(self, s, start, pattern):
        if start == len(s):
            return True 
        
        if start > len(s):
            return False
            
        if s[start: start + len(pattern)] == pattern:
            ret = self.dfs(s, start + len(pattern), pattern)
            if ret:
                return True 
        return False        