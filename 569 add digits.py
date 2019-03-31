class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        while num:
            cur = num
            total = 0
            while cur > 0:
                total += cur % 10
                cur //= 10 
            if total < 10:
                return total 
            num = total
        return 0
        
