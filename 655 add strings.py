class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        n1 = 0
        for char in num1:
            n1 = n1 * 10 + int(char)
        
        n2 = 0 
        for char in num2:
            n2 = n2 * 10 + int(char)
            
        return str(n1 + n2)