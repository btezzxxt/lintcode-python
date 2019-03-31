class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    _roman = {
        "M": ["" ,"M", "MM", "MMM"],
        "C": ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        "X": ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        "I": ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    }

    def intToRoman(self, n):
        # write your code here
        return self._roman["M"][n // 1000] + self._roman["C"][n // 100 % 10] + self._roman["X"][n // 10 % 10] + self._roman["I"][n % 10]
