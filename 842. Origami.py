class Solution:
    """
    @param n: The folding times
    @return: the 01 string
    """
    def getString(self, n):
        # Write your code here
        return "".join(self.helper(n))
    
    def helper(self, n):
        if n == 1:
            return ["0"]
        
        arr = self.getString(n - 1)
        res = []
        for i, char in enumerate(arr):
            if i % 2 == 0:
                res.append("0")
            else:
                res.append("1")
            res.append(char)
        res.append("1")
        return res
            