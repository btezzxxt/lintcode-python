# class Solution:
#     """
#     @param str: A string
#     @return: all permutations
#     """
#     def stringPermutation2(self, str):
#         # write your code here
#         str_arr = sorted(str)
#         res = []
#         self.dfs(str_arr, [], set(), res)
#         return res

#     def dfs(self, str_arr, path, visited_index, res):
#         if len(str_arr) == len(path):
#             res.append(''.join(path))
#             return 
        
#         for i in range(len(str_arr)):
#             if i in visited_index:
#                 continue
            
#             if i > 0 and str_arr[i] == str_arr[i - 1] and i - 1 not in visited_index:
#                 continue
            
#             visited_index.add(i)
#             path.append(str_arr[i])
#             self.dfs(str_arr, path, visited_index, res)
#             path.pop()
#             visited_index.remove(i)
    
# print(Solution().stringPermutation2("abb"))


class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        str_arr = list(str)
        str_arr.sort()
        res = []
        self.dfs(str_arr, res, [], set())
        return res

    def dfs(self, str_arr, res, path, visited_i):
        if len(path) == len(str_arr):
            res.append("".join(path))
            return 
        
        for i in range(len(str_arr)):
            if i in visited_i:
                continue
            
            if i > 0 and str_arr[i] == str_arr[i - 1] and i - 1 not in visited_i:
                continue
            
            path.append(str_arr[i])
            visited_i.add(i)
            self.dfs(str_arr, res, path, visited_i)
            visited_i.remove(i)
            path.pop()

        