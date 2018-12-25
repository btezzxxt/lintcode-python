class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = list(set(candidates))
        candidates.sort()
        
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res
    
    def dfs(self, candidates, start, remain, path, res):
        if remain < 0 or start == len(candidates):
            return 
        
        if remain == 0:
            res.append(list(path))
            return

        path.append(candidates[start])
        self.dfs(candidates, start, remain - candidates[start], path, res)
        path.pop()

        self.dfs(candidates, start + 1, remain, path, res)
