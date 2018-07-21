class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        max = 2147483647

        if divisor == 0:
            return 2147483647
        if dividend == 0:
            return 0

        positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        
        divisor = abs(divisor)
        dividend = abs(dividend)

        quotient = 0
        while divisor <= dividend:
            offset = 0
            while divisor << offset <= dividend:
                offset += 1
            dividend -= divisor << (offset - 1)
            quotient += 1 << (offset - 1)

        quotient = quotient if positive else -quotient
        if quotient > max:
            quotient = max
        elif quotient < -max - 1:
            quotient = -max - 1

        return quotient 

print(Solution().divide(10, 3))