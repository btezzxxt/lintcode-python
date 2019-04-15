class Solution:
    """
    @param num: a non-negative integer N
    @return: the largest number that is less than or equal to N with monotone increasing digits.
    """
    def monotoneDigits(self, num):
        # write your code here
        digits = [0] * 10 
        cnt = 0 
        
        while num:
            digits[cnt] = num % 10 
            cnt += 1 
            num //= 10
        
        pos = 0
        for i in range(1, cnt):
            if digits[i] >digits[i - 1]:
                pos = i 
                digits[i] = digits[i] - 1 
            
        for i in range(pos):
            digits[i] = 9 
        
        res = 0
        for i in range(cnt - 1, -1, -1):
            res = res * 10 + digits[i]
        return res 
        
        