class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    # dp 解法 在0 - i 之间去取最大的可以满足grid[i] % grid[j] 的dp[j] + 1 之后将j存为i的father
    # 另外设置两个global变量 一个计最大数 一个记录最大位置index
    # 最后再从index 一步步推回去 
    def largestDivisibleSubset(self, grid):
        grid.sort()
        dp = [1] * len(grid)
        father = [-1] * len(grid)

        max_value = 1
        max_index = 0

        for i in range(len(grid)):
            for j in range(0, i):
                if grid[i] % grid[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    father[i] = j
                    if dp[i] > max_value:
                        max_value = dp[i]
                        max_index = i

        res = []
        while max_value > 0:
            res.append(grid[max_index])
            max_index = father[max_index]
            max_value -= 1
        return res

print(Solution().largestDivisibleSubset([1,2,3]))

    # # dfs + memo 解法， 超时
    # def largestDivisibleSubset(self, grid):
    #     # write your code here
    #     res = [set([num]) for num in grid]
    #     memo = {}
    #     self.dfs(grid, 0, [], res, memo)
        
    #     largest = list(self.select_largest(res))
    #     return largest
    
    # def dfs(self, grid, start, pair, res, memo):
    #     if len(pair) == 2:
    #         if self.is_valid(pair[0], pair[1], memo):
    #             self.add_to_res(res, pair, memo)
    #         return
        
    #     for i in range(start, len(grid)):
    #         pair.append(grid[i])
    #         self.dfs(grid, i + 1, pair, res, memo)
    #         pair.pop()

    # def add_to_res(self, res, pair, memo):
    #     for i, set_ in enumerate(res):
    #         should_add = True
    #         for num in set_:
    #             if self.is_valid(num, pair[0], memo) and self.is_valid(num, pair[1], memo):
    #                 continue
    #             else:
    #                 should_add = False
    #         if should_add:
    #             print(pair)
    #             res[i] = set_.union(pair)

    #     res.append(set(pair))       

    # def is_valid(self, a, b, memo):
    #     if a > b:
    #         a, b = b, a
    #     if (a, b) in memo:
    #         return memo[(a,b)]

    #     res = a % b == 0 or b % a == 0
    #     memo[(a, b)] = res
    #     return res


    # def select_largest(self, res):
    #     largest = set()
    #     max_len = -1
    #     for set_ in res:
    #         if len(set_) > max_len:
    #             largest = set_
    #             max_len = len(set_)
    #     return largest
