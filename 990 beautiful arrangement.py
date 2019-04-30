class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    count = 0
    def countArrangement(self, N):
        # Write your code here
        self.dfs(set(), 1, N)
        return self.count
        
    def dfs(self, res, i, N):
        if i > N:
            self.count += 1
            return
        
        for num in range(1, N + 1):
            if num not in res and (num % i == 0 or i % num == 0):
                res.add(num)
                self.dfs(res, i + 1, N)
                res.remove(num)