class Solution:
    """
    @param source: the input string
    @return: the number of subsequences 
    """
    def countSubsequences(self, source):
        # write your code here
        # 傻逼数学题
        a_cnt = 0
        b_cnt = 0
        c_cnt = 0
        
        for char in source:
            if char == "a":
                a_cnt = 1 + 2 * a_cnt
            elif char == "b":
                b_cnt = a_cnt + 2 * b_cnt
            elif char == "c":
                c_cnt = b_cnt + 2 * c_cnt
        return c_cnt