class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    # 记忆化搜索经典
    def isMatch(self, s, p):
        # write your code here
        return self.dfs(s, p, 0, 0, {})

    # devide and conquar, return true or false
    def dfs(self, s, p, i, j, visited):
        if (i, j) in visited:
            return visited[(i, j)]

        if len(p) == j and len(s) == i:
            return True
        
        if len(p) == j:
            return False
        
        if len(s) == i:
            for c in range(j, len(p)):
                if p[c] != '*':
                    return False
            return True
        
        l = s[i]
        r = p[j]

        if r != '*':
            res = self.letter_match(l, r) and self.dfs(s, p, i + 1, j + 1, visited)
        else:
            res = self.dfs(s, p, i + 1, j, visited) or \
                    self.dfs(s, p, i, j + 1, visited)
    
        visited[(i, j)] = res
        return res
        
    def letter_match(self, l, r):
        if l == r or r == "?" or r == "*":
            return True
        return False

print(Solution().isMatch("aa", "aa"))

class Solution2:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        return self.dfs(s, p, {})
        
    def dfs(self, s, p, memo):
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) == 0:
            if p == "*":
                return True
            else:
                return False
        elif len(p) == 0:
            return False
            
        if (s, p) in memo:
            return memo[(s, p)]
        
        char = p[0]
        if char != '*':
            res = self.char_match(s[0], char) and self.dfs(s[1:], p[1:], memo)
        else:
            res = self.dfs(s[1: ], p, memo) or self.dfs(s, p[1: ], memo)
            
        memo[(s, p)] = res    
        return res
            
    def char_match(self, c1, c2):
        return c1 == c2 or c2 == "?" or c2 == "*"
            