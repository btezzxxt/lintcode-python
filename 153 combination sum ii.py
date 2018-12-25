class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        res = []
        self.dfs(num, 0, [], res, target)
        return res

    def dfs(self, num, start, path, res, remain):
        if remain == 0:
            res.append(list(path))
            return 
        
        if start == len(num) or remain < 0:
            return 

        for i in range(start, len(num)):
            if start != i and i > 0 and num[i] == num[i - 1]:
                continue
            path.append(num[i])
            self.dfs(num, i + 1, path, res, remain - num[i])
            path.pop()

