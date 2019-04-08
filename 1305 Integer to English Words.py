class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        # Write your code here
        res = self.convert_hundreds(num % 1000)
        m1 = ["Thousand", "Million", "Billion"]
        for i in range(3):
            num = num // 1000
            if num > 0:
                temp = self.convert_hundreds(num % 1000)
                res = temp + " " + m1[i] + " " + res 
        if res.strip() == "":
            return "Zero"
        return res.strip()
    
    def convert_hundreds(self, num):
        a = num // 100
        b = num % 100
        c = num % 10
        
        m1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", \
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        m2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        res = ""
        if a > 0:
            res = m1[a] + " Hundred"
        
        if b < 19:
            res += " " + m1[b]
        else:
            res += " " + m2[b // 10]
            res += " " + m1[c]
        return res.strip()
        