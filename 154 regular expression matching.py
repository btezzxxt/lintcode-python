# class Solution:
#     """
#     @param s: A string 
#     @param p: A string includes "." and "*"
#     @return: A boolean
#     """
#     def isMatch(self, s, p):
#         # write your code here
#         return self.dfs(s, p, 0, 0, {})
    
#     # devide and conquer + 记忆化搜索, return 从i， j开始匹配的字符串结果
#     def dfs(self, s, p, i, j, memo):
#         # 记忆化搜索不能忘了查找map
#         if (i, j) in memo:
#             return memo[(i, j)]

#         if len(s) == i and len(p) == j:
#             return True
        
#         if len(p) == j:
#             return False
        
#         if len(s) == i:
#             return self.is_empty(p[j:])

#         l = s[i]
#         r = p[j]

#         res = False
#         if j + 1 < len(p) and p[j + 1] == '*':
#             # a* matches empty or a* matches more than one
#             res = self.dfs(s, p, i, j + 2, memo) or (self.check_match(l, r) and self.dfs(s, p, i + 1, j, memo))      
#         else:
#             res = self.check_match(l, r) and self.dfs(s, p, i + 1, j + 1, memo)

#         # 记下结果
#         memo[(i, j)] = res
#         return res

#     def check_match(self, a, b):
#         return a == b or b == '.'

#     def is_empty(self, string):
#         if len(string) % 2 != 0:
#             return False

#         for i in range(len(string)):
#             if i % 2 == 1 and (string[i] != '*' or string[i-1] == '*'):
#                 return False
#         return True
 

# print(Solution().isMatch("ab", ".*c"))

class Solution2:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        return self.dfs(s, p, {})

    def dfs(self, s, p, memo):
        if (s, p) in memo:
            return memo[(s, p)]
        
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) == 0:
            if len(p) % 2 == 1:
                return False
            for i, char in enumerate(p):
                if i % 2 == 0 and p[i] == '*':
                    return False
                if i % 2 == 1 and p[i] != '*':
                    return False
            return True
        elif len(p) == 0:
            return False
        
        s_cur = s[0]
        if len(p) == 1 or (len(p) > 1 and p[1] != '*'):
            p_cur = p[0]
            res = self.char_match(s_cur, p_cur) and self.dfs(s[1: ], p[1: ], memo)
        else:
            p_cur = p[0: 2]
            res = self.dfs(s, p[2: ], memo) or (self.char_match(s_cur, p_cur) and self.dfs(s[1: ], p, memo))
        
        memo[(s, p)] = res 
        return res
    
    def char_match(self, c1, c2):
        if len(c2) == 1:
            if c1 == c2 or c2 == '.':
                return True
            else:
                return False
        else:
            if c1 == c2[0] or c2[0] == '.':
                return True
            else:
                return False
print(Solution().isMatch("ab", ".*c"))

            