class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        
        num += 1 
        res = [] 
        while num:
            res.append(num % 10)
            num = num // 10 
        res.reverse()
        return res 