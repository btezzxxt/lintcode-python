class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    # 记忆化搜索解区间化dp经典例题
    def maxCoins(self, nums):
        # write your code here
        n = len(nums)
        A = [1] * (n + 2)
        for i in range(n):
            A[i + 1] = nums[i]

        dp = [[0] * (n + 1) for i in range(n + 1)]
        visited = [[0] * (n + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][i] = A[i - 1] * A[i] * A[i + 1]
            visited[i][i] = 1

        coins = self.search(1, n, dp, A, visited)
        return coins 
    
    def search(self, i, j, dp, A, visited):
        if i > j:
            return 0
        
        if visited[i][j] == 1:
            return dp[i][j]
        
        max_coins = 0
        for k in range(i, j + 1):
            coins = self.search(i, k - 1, dp, A, visited) + self.search(k + 1, j, dp, A, visited) + A[i - 1] * A[k] * A[j + 1]
            if coins > max_coins:
                max_coins = coins

        dp[i][j] = max_coins
        visited[i][j] = 1
        return dp[i][j]