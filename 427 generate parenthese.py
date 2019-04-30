class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        res = []
        self.dfs(res, [], 0, 0, n)
        return res 
        
        
    def dfs(self, res, path, left, right, n):
        if left == n and right == n:
            res.append("".join(path))
            return 
        
        if left < n:
            path.append("(")
            self.dfs(res, path, left + 1, right, n)
            path.pop()
        
        if right < n and left > right:
            path.append(")")
            self.dfs(res, path, left, right + 1, n)
            path.pop()