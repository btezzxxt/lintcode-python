class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        if n == 0:
            return [0]
        
        prev = self.grayCode(n - 1)
        
        res = []
        for seq in prev:
            res.append(seq)
        
        for seq in reversed(prev):
            res.append(1 << (n - 1) | seq)
        return res 
        