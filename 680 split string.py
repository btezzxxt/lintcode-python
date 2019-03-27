# class Solution:
#     """
#     @param: : a string to be split
#     @return: all possible split string array
#     """

#     def splitString(self, s):
#         # write your code here
#         res = []
#         self.dfs(0, s, [], res)
#         return res
    
#     def dfs(self, i, s, path, res):
#         # 又忘了return
#         if i == len(s):
#             res.append(list(path))
#             return 
        
#         # 这里不用for循环 因为这是找从每个i开始的情况 而不是对于从i开始的情况
#         path.append(s[i])
#         self.dfs(i + 1, s, path, res)
#         path.pop()

#         if i + 1 < len(s):
#             path.append(s[i: i+2])
#             self.dfs(i + 2, s, path, res)
#             path.pop()

# print(Solution().splitString("123"))

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, idx, path, res):
        if idx >= len(s):
            res.append(path)
            return 

        path.append(s[idx])
        self.dfs(s, idx + 1, path, res)
        path.pop()

        if idx < len(s) - 1:
            path.append(s[idx: idx + 2])
            self.dfs(s, idx + 2, path, res)
            path.pop()

print(Solution().splitString("123"))
        