class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        return self.dfs(s, p, 0, 0, {})
    
    # devide and conquer + 记忆化搜索, return 从i， j开始匹配的字符串结果
    def dfs(self, s, p, i, j, memo):
        # 记忆化搜索不能忘了查找map
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i and len(p) == j:
            return True
        
        if len(p) == j:
            return False
        
        if len(s) == i:
            return self.is_empty(p[j:])

        l = s[i]
        r = p[j]

        res = False
        if j + 1 < len(p) and p[j + 1] == '*':
            # a* matches empty or a* matches more than one
            res = self.dfs(s, p, i, j + 2, memo) or (self.check_match(l, r) and self.dfs(s, p, i + 1, j, memo))      
        else:
            res = self.check_match(l, r) and self.dfs(s, p, i + 1, j + 1, memo)

        # 记下结果
        memo[(i, j)] = res
        return res

    def check_match(self, a, b):
        return a == b or b == '.'

    def is_empty(self, string):
        if len(string) % 2 != 0:
            return False

        for i in range(len(string)):
            if i % 2 == 1 and (string[i] != '*' or string[i-1] == '*'):
                return False
        return True
 

print(Solution().isMatch("ab", ".*c"))