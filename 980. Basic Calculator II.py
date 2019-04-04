import re
class Solution:
    def calculate(self, s):
        stack = []
        num = ""
        sign = ""
        for i, char in enumerate(s):
            if char in "+-*/":
                sign = char
            elif self.is_number(char):
                num += char
                if i + 1 >= len(s) or not self.is_number(s[i + 1]):
                    value = int(num)
                    if not stack:
                        stack.append(value)
                    else:
                        if sign == "-":
                            stack.append(-value)
                        elif sign == "+":
                            stack.append(value)
                        else:
                            stack.append(self.calculate_last(stack.pop(), value, sign))
                        sign = ""                        
                    num = ""
            else:
                continue
        return sum(stack)

    def is_number(self, char):
        return re.match(r"[0-9]", char)

    def calculate_last(self, a, b, op):
        result = 0
        if op == "*":
            result = a * b 
        elif op == "/":
            result = a / b
            if result < 0:
                result = math.ceil(result)
            else:
                result = math.floor(result)
        return result
        
