import re
class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # write your code here
        if str == "":
            return 0
        
        str = str.strip()
        INT_MAX = (1 << 31) - 1 
        INT_MIN = -1 << 31 
        
        sign = 1 
        start = 0
        if str[0] == "-":
            sign = -1
            start = 1 
        elif str[0] == "+":
            sign = 1 
            start = 1 
        
        num = 0
        for i in range(start, len(str)):
            char = str[i]
            if not re.match(r"[0-9]", char):
                break 
            
            num = num * 10 + int(char)
            if num > INT_MAX:
                return INT_MAX if sign > 0 else INT_MIN 
        return num * sign    
        
            
            