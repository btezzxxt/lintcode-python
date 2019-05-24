class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        # 学一手分治法 ***
        if n > 0:
            return self.possivePow(x, n)
        else:
            return self.possivePow(1/x, -n)

    def possivePow(self, x, n):
        if n == 0:
            return 1
        
        half = self.possivePow(x, n//2)
        # 失误 不可以把递归写4次，存进half 只递归一次 
        # 否则分治的时间复杂度就不是logn了，而是O（n） 

        if abs(half) < 1e-5:
            return 0

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


print(Solution().myPow(2, -2147483648))

class Solution2:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1 
        elif n < 0:
            return 1 / self.calc_pow(x, -n)
        else:
            return self.calc_pow(x, n)
        
    
    def calc_pow(self, x, n):
        if n == 0:
            return 1
                
        half = self.calc_pow(x, n // 2)
        if n % 2 == 1:
            return half * half * x 
        else:
            return half * half


class Solution2:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.calc(x, -n)
        else:
            return self.calc(x, n)
    
    def calc(self, x, n):
        # later
        if n == 0:
            return 1 
        
        half = self.calc(x, n // 2)
        if n % 2 == 0:
            return half * half 
        else:
            return half * half * x
        

print(Solution2().myPow(8.84372, -5))