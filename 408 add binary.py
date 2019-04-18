class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        if a == "":
            return b 
        
        if b == "":
            return a 
        
        if len(a) > len(b):
            a, b = b, a 
        
        res = []
        offset = 0
        for i in range(1, len(a) + 1):
            sum = int(a[-i]) + int(b[-i]) + offset
            if sum == 3:
                res.append("1")
                offset = 1
            elif sum == 2:
                res.append("0")
                offset = 1 
            elif sum == 1:
                res.append("1")
                offset = 0
            else:
                res.append("0")
                offset = 0 
        
        for i in range(len(b) - len(a) - 1, -1, -1):
            sum = int(b[i]) + offset
            if sum == 2:
                res.append("0")
                offset = 1 
            elif sum == 1:
                res.append("1")
                offset = 0
            elif sum == 0:
                res.append("0")
                offset = 0
                
        if offset == 1:
            res.append("1")
                
        res.reverse()
        
        return "".join(res)