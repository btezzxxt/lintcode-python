class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, i, path, result):
        if i == len(nums):
            result.append(list(path))
            return 

        path.append(nums[i])
        self.dfs(nums, i + 1, path, result)
        path.pop()

        self.dfs(nums, i + 1, path, result)

print(Solution().subsets([0]))