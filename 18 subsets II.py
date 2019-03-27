class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, path, res):
        res.append(list(path))
        
        for i in range(start, len(nums)):
            if start != i and nums[i] == nums[i - 1]:
                continue
            else:
                path.append(nums[i])
                self.dfs(nums, i + 1, path, res)
                path.pop()

print(Solution().subsetsWithDup([1,1]))
# 重点题