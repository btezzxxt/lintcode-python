class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx >= len(s):
            res.append(path[::])
            return 
        
        for i in range(idx, len(s)):
            cur = s[idx: i + 1]
            if self.is_palindrome(cur):
                path.append(cur)
                self.dfs(s, i + 1, path, res)
                path.pop()
          
    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True