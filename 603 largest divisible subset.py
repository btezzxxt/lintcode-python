class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    # dfs + memo 解法， 超时
    def largestDivisibleSubset(self, grid):
        # write your code here
        res = [set([num]) for num in grid]
        memo = {}
        self.dfs(grid, 0, [], res, memo)
        
        largest = list(self.select_largest(res))
        return largest
    
    def dfs(self, grid, start, pair, res, memo):
        if len(pair) == 2:
            if self.is_valid(pair[0], pair[1], memo):
                self.add_to_res(res, pair, memo)
            return
        
        for i in range(start, len(grid)):
            pair.append(grid[i])
            self.dfs(grid, i + 1, pair, res, memo)
            pair.pop()

    def add_to_res(self, res, pair, memo):
        for i, set_ in enumerate(res):
            should_add = True
            for num in set_:
                if self.is_valid(num, pair[0], memo) and self.is_valid(num, pair[1], memo):
                    continue
                else:
                    should_add = False
            if should_add:
                print(pair)
                res[i] = set_.union(pair)

        res.append(set(pair))       

    def is_valid(self, a, b, memo):
        if a > b:
            a, b = b, a
        if (a, b) in memo:
            return memo[(a,b)]

        res = a % b == 0 or b % a == 0
        memo[(a, b)] = res
        return res


    def select_largest(self, res):
        largest = set()
        max_len = -1
        for set_ in res:
            if len(set_) > max_len:
                largest = set_
                max_len = len(set_)
        return largest
