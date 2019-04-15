import re
class Solution:
    """
    @param a: a string
    @param b: a string
    @return: a string representing their multiplication
    """
    def complexNumberMultiply(self, a, b):
        # Write your code here
        # (x+yi) * (m+ni)
        # output: xm - yn + (xn + ym)i 
        a = a[: -1]
        b = b[: -1]
        [temp1, temp2] = re.split(r"[+]", a)
        x = int(temp1)
        y = int(temp2)
        
        [temp1, temp2] = re.split(r"[+]", b)
        m = int(temp1)
        n = int(temp2)
        
        part1 = x * m - y * n
        part2 = x * n + y * m 
        
        res = [str(part1)]
        res.append("+")
        res.append(str(part2))
        res.append("i")
        
        return "".join(res)
        
        
        