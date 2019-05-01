class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here
        val1 = 0
        for char in num1:
            val1 = val1 * 10 + int(char)
        
        val2 = 0 
        for char in num2:
            val2 = val2 * 10 + int(char)
        
        res = val1 * val2 
        arr = []
        while res:
            arr.append(str(res % 10))
            res //= 10 
        arr.reverse()
        
        if not arr:
            return "0"
        return "".join(arr)
        
        
