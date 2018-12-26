class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        self.dfs(nums, [], set(), res)
        return res
    
    def dfs(self, nums, path, used, res):
        if len(path) == len(nums):
            return res.append(list(path))

        for num in nums:
            if num not in used:
                path.append(num)
                used.add(num)
                self.dfs(nums, path, used, res)
                used.remove(num)
                path.pop()
        

