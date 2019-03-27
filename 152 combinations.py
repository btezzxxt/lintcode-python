class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        res = []
        self.dfs(n, k, 1, [], res)
        return res
        
    def dfs(self, n, k, start, path, res):
        if len(path) == k:
            res.append(list(path))
            return 
        
        for i in range(start, n + 1):       
            path.append(i)
            self.dfs(n, k, i + 1, path, res)
            path.pop()

# 两种办法
# class Solution:
#     """
#     @param n: Given the range of numbers
#     @param k: Given the numbers of combinations
#     @return: All the combinations of k numbers out of 1..n
#     """
#     def combine(self, n, k):
#         # write your code here
#         res = []
#         self.dfs(n, k, 1, [], res)
#         return res
        
#     def dfs(self, n, k, start, path, res):
#         if len(path) == k:
#             res.append(list(path))
#             return 
        
#         if len(path) > k or start > n:
#             return 
        

        
#         path.append(start)
#         self.dfs(n, k, start + 1, path, res)
#         path.pop()

#         self.dfs(n, k, start + 1, path, res)            

print(Solution().combine(2,1))

class Solution2:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        res = []
        self.dfs(1, n, [], res, k)
        return res
    
    def dfs(self, i, n, path, res, k):
        if len(path) == k:
            res.append(path[::])
        
        for num in range(i, n + 1):
            path.append(num)
            self.dfs(num + 1, n, path, res, k)
            path.pop()
        
