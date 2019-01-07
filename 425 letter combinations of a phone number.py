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
        res = []
        self.dfs(digits, 0, [], res)
        return res 
    
    def dfs(self, digits, i, path, res):
        if i == len(digits):
            if len(path) > 0:
                res.append("".join(path))
            return 
        
        digit = digits[i]
        letters = self.mapping[digit]
        for l in letters:
            path.append(l)
            self.dfs(digits, i + 1, path, res)
            path.pop()
    
