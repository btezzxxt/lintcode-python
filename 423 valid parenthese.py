class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    
    _parenthese_map = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    
    _p_open = set(_parenthese_map.values())
    _p_close = set(_parenthese_map.keys())
    
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for char in s:
            print(char)
            if self.is_open(char):
                stack.append(char)
            elif self.is_close(char):
                if not stack or not self.match(stack[-1], char):
                    return False 
                else:
                    stack.pop()
            else:
                return False
        
        if len(stack) > 0:
            return False
            
        return True
        
    def is_open(self, char):
        if char in self._p_open:
            return True
        return False
    
    def is_close(self, char):
        if char in self._p_close:
            return True
        return False
    
    def match(self, open, close):
        if self._parenthese_map[close] == open:
            return True
        return False
                    
