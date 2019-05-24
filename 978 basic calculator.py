import re
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        stack = [] 
        sign = 1 # 1 for + -1 for -
        res = 0 
        num = 0
        for char in s:
            if char in "0123456789":
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                sign = 1
                num = 0 
            elif char == '-':
                res += sign * num 
                sign = -1 
                num = 0 
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1 
                res = 0 
            elif char == ')':
                res += sign * num 
                num = 0 
                sign = 1 
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
                
                
        
        