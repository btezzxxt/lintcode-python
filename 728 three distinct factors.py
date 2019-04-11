import math
class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """
    def isThreeDisctFactors(self, n):
        # write your code here
        root = math.sqrt(n)
        factor = int(root)
        
        if root != factor:
            return False 
        return self.is_prime(factor)
        
    def is_prime(self, factor):
        if factor < 2:
            return False
        
        maxi_factor = math.sqrt(factor)
        for i in range(2, int(maxi_factor)):
            if factor % i == 0:
                return False 
        return True
        
        