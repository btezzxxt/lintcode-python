import math
class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        # Write your code here
        # 必须要处理0
        if n == 0:
            return False
        
        diff = 10e-12
        
        res = math.log(n) / math.log(3)
        if abs(res - round(res)) < diff:
            return True
        return False