import re
class Solution:
    """
    @param equation: a string
    @return: return a string
    """
    def solveEquation(self, equation):
        # write your code here
        [left, right] = equation.split('=')
        left_x, left_val = self.process(left)
        right_x, right_val = self.process(right)
        if left_x == right_x and left_val == right_val:
            return "Infinite solutions"
        elif left_x == right_x:
            return "No solution"
        else:
            co_x = left_x - right_x
            val = right_val - left_val
            return "x=" + str(val // co_x)
            
    def process(self, exp):
        i = 0 
        n = len(exp)
        op = 1
        num = None
        
        co_x = 0
        co_val = 0
        while i < n:
            char = exp[i]
            if char == "+":
                op = 1 
            elif char == "-":
                op = -1 
            elif char == "x":
                if num == None:
                    num = 1
                num = num * op 
                co_x += num 
                num = None 
            elif re.match(r"[0-9]", char) and i + 1 == n or (exp[i + 1] in "+-"):
                if num == None:
                    num = int(char)
                else:
                    num = num * 10 + int(char)
                num = num * op
                co_val += num
                num = None 
            else:
                if num == None:
                    num = int(char)
                else:
                    num = num * 10 + int(char)
            i += 1 
        return co_x, co_val
                    
import re
class Solution2:
    """
    @param equation: a string
    @return: return a string
    """
    def solveEquation(self, equation):
        # write your code here
        [left, right] = equation.split('=')
        left_x, left_val = self.process(left)
        right_x, right_val = self.process(right)
        if left_x == right_x and left_val == right_val:
            return "Infinite solutions"
        elif left_x == right_x:
            return "No solution"
        else:
            co_x = left_x - right_x
            val = right_val - left_val
            return "x=" + str(val // co_x)
            
    def process(self, exp):
        if exp[0] not in "-+":
            exp = "+" + exp 
        
        parts = re.split(r"[+-]", exp)
        parts = parts[1:]
        ops = re.findall(r"[+-]", exp)
        
        print(parts, ops)
        coef_x = 0
        coef_val = 0
        
        for i in range(len(parts)):
            op = 1 if ops[i] == "+" else -1
            part = parts[i]
            if part[-1] == "x":
                val = 1 if part[: -1] == "" else int(part[: -1])
                coef_x += op * int(val)
            else:
                coef_val += op * int(part)
                
        return coef_x, coef_val                
                
                
                
                
                    