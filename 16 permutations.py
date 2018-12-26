class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        res = []
        self.dfs(nums, [], set(), res)
        return res
    
    def dfs(self, nums, path, usedIndex, res):
        if len(path) == len(nums):
            res.append(list(path))
            return
        
        for j in range(len(nums)):
            if j in usedIndex:
                continue

            # 去重的方法 sort之后 当需要选一个数字的时候 如果前一个数字和它相同 优先前一个
            if j > 0 and nums[j] == nums[j - 1] and j - 1 not in usedIndex:
                continue
            
            path.append(nums[j])
            usedIndex.add(j)
            self.dfs(nums, path, usedIndex, res)
            usedIndex.remove(j)
            path.pop()

        
            
