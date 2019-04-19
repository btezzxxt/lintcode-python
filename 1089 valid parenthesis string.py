class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        # Write your code here
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == "(":
                min_open += 1 
                max_open += 1
            else:
                min_open -= 1 
                if min_open < 0:
                    min_open = 0
            
                if char != ")":
                    max_open += 1
                else:
                    max_open -= 1 
                    if max_open < 0:
                        return False 
        
        if min_open > 0:
            return False 
        return True