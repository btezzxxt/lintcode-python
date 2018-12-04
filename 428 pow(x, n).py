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