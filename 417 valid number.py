import re
class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        # write your code here
        s = s.strip()
        
        integer = re.compile(r"^[+-]?[0-9]+$")
        decimal = re.compile(r"^[+-]?(([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*))$")
        e = re.compile(r"^[+-]?[0-9]+e?[+-][0-9]+$")
        
        if integer.match(s) or decimal.match(s) or e.match(s):
            return True 
        return False