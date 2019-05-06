import re
class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str):
        # Write your code here
        arr = list(str)
        arr.sort()
        
        res = [] 
        count = 0
        for char in arr:
            if re.match(r'[0-9]', char):
                count += int(char)
            else:
                res.append(char)
        res.append(self.num_to_str(count))
        return "".join(res)
    
    def num_to_str(self, num):
        res = []
        while num:
            res.append(str(num % 10))
            num = num // 10
        res.reverse()
        return "".join(res)