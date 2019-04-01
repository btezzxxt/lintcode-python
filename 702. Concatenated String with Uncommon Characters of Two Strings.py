class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        s2_chars = set(list(s2))
        shared_chars = set()
        res = []
        for char in s1:
            if char in s2_chars:
                shared_chars.add(char)
            else:
                res.append(char)

        for char in s2:
            if char not in shared_chars:
                res.append(char)
        return ''.join(res)