import math
import re
class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calcualte_without_p(self, s):
        stack = []
        num = ""
        sign = []
        
        for i, char in enumerate(s):
            if self.is_number(char):
                num += char
                if i + 1 == len(s) or not self.is_number(s[i + 1]):
                    val = int(num)
                    if not sign:
                        stack.append(val)
                    elif sign[-1] == "+":
                        stack.append(val)
                    elif sign[-1] == "-":
                        stack.append(-val)
                    elif sign[-1] == "*":
                        first = stack.pop()
                        stack.append(first * val)
                    elif sign[-1] == "/":
                        first = stack.pop()
                        res = first / val
                        if res > 0:
                            stack.append(math.floor(res))
                        else:
                            stack.append(math.ceil(res))
                    if sign:
                        sign.pop()
                    num = ""
            elif char in "+-*/":
                sign.append(char)
            else:
                continue
        return sum(stack)

    
    def calculate(self, s):
        # Write your code here
        stack = []
        
        for i, char in enumerate(s):
            if char == " ":
                continue
            elif char == "(":
                stack.append(char)
            elif char == ")":
                string = []
                while stack and stack[-1] != "(":
                    string.append(stack.pop())
                string.reverse()
                val = self.calcualte_without_p("".join(string))

                if stack and stack[-1] == "(":
                    stack.pop()
                stack.append(str(val))
            else:
                stack.append(char)
        string = []    
        while stack:
            string.append(stack.pop())
        string.reverse()
        return self.calcualte_without_p("".join(string))
        
    def is_number(self, char):
        return re.match(r"[0-9]", char)

print(Solution().calcualte_without_p("1*2-3/4+5*6-7*8+9/10"))