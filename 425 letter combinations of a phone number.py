# class Solution:
#     """
#     @param digits: A digital string
#     @return: all posible letter combinations
#     """
#     mapping = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz"
#     }


#     def letterCombinations(self, digits):
#         # write your code here
#         res = []
#         self.dfs(digits, 0, [], res)
#         return res 
    
#     def dfs(self, digits, i, path, res):
#         if i == len(digits):
#             if len(path) > 0:
#                 res.append("".join(path))
#             return 
        
#         digit = digits[i]
#         letters = self.mapping[digit]
#         for l in letters:
#             path.append(l)
#             self.dfs(digits, i + 1, path, res)
#             path.pop()
    
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits):
        # write your code here
        if digits == "":
            return []
        
        res = self.dfs(digits, {})
        return res


    def dfs(self, digits_left, memo):
        if len(digits_left) == 0:
            return ['']

        if digits_left in memo:
            return memo[digits_left]
        
        digit = digits_left[0]
        
        combo = self.dfs(digits_left[1: ], memo)
        res = []
        for char in self.mapping[digit]:
            for string in combo:
                res.append(char + string)
        
        memo[digits_left] = res
        return res




