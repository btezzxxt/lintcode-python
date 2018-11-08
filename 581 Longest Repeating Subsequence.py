class Solution:
    """
    @param str: a string
    @return: the length of the longest repeating subsequence
    """
    def longestRepeatingSubsequence(self, str):
        # write your code here
        if len(str) == 0:
            return 0

        n = len(str)

        f = [[0] * n for i in range(n)]

        for i in range(1, n):
            if f[0][i-1] == 0 and str[i] == str[0]:
                f[0][i] = 1
            elif f[0][i-1] == 1:
                f[0][i] = 1
        
        for i in range(1, n):
            f[i][0] = f[0][i]

        for i in range(1, n):
            for j in range(1, n):
                if str[i] != str[j] or i == j:
                    f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1]) 
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        
        return f[-1][-1]

Solution().longestRepeatingSubsequence("aab")