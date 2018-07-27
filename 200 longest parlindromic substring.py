class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    # def longestPalindrome(self, s):
    #     # write your code here
    #     if len(s) == 0 or len(s) == 1:
    #         return s
        
    #     max_ = 1
    #     start = 0
    #     for i in range(len(s)):
    #         l1 = self.getPalindromeLength(s, i, i)
    #         if l1 > max_:
    #             max_ = l1
    #             start = i - max_ // 2
            
    #         l2 = self.getPalindromeLength(s, i, i+1)
    #         if l2 > max_:
    #             max_ = l2
    #             start = i - max_ // 2 + 1
    #     return s[start: start + max_]
        
    # def getPalindromeLength(self, s, i, j):
    #     len_ = 0
    #     while 0 <= i and j < len(s) and s[i] == s[j]:
    #         if i == j:
    #             len_ = 1
    #         else:
    #             len_ += 2
    #         i -= 1
    #         j += 1
    #     return len_

    def longestPalindrome(self, s):
        len_ = len(s)
        if len_ == 0 or len_ == 1:
            return s
        
        f = [[False] * len_ for i in range(len_)]

        for i in range(len_):
            f[i][i] = True
        
        for i in range(len_ - 1):
            if s[i] == s[i + 1]:
                f[i][i+1] = True

        for j in range(2, len_):
            for i in range(j - 2, -1, -1):
                if f[i+1][j-1] == True and s[i] == s[j]:
                    f[i][j] = True

        start = 0
        max_ = 0
        for j in range(1, len(f)):
            for i in range(0, j):
                if f[i][j] and j - i + 1 > max_:
                    start = i
                    max_ = j - i + 1
        return s[start: start + max_]

print(Solution().longestPalindrome("ccc"))
        

