# # 遍历中轴线
# class Solution:
#     """
#     @param s: input string
#     @return: the longest palindromic substring
#     """
#     def longestPalindrome(self, s):
#         # write your code here
#         if s == "":
#             return ""
    
#         longest = 1
#         start = 0
#         for i in range(len(s)):
#             leng = self.findPalindrome(s, i, i)
#             if leng > longest:
#                 start = i - leng // 2
#                 longest = leng
            
#             leng = self.findPalindrome(s, i, i+1)
#             if leng > longest:
#                 start = i - leng // 2 + 1
#                 longest = leng

#         return s[start: start + longest]

#     def findPalindrome(self, s, start, end):
#         while start >= 0 and end < len(s) and s[start] == s[end]:
#             start -= 1
#             end += 1
#         return end - start + 1 - 2

# print(Solution().longestPalindrome("abcddcbg"))

# dp 用isPalindrome 二维数组记录i到j的substring是否是palindrome
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if s == "":
            return ""
        l = len(s)
        isPalindrome = [[0] * l for i in range(l)]

        longest = 1
        start = 0

        # 初始化
        for i in range(l):
            isPalindrome[i][i] = 1
        
        for i in range(l-1):
            if s[i] == s[i+1]: 
                isPalindrome[i][i+1] = 1
                longest = 2
                start = i
        
        # 记忆化搜索
        for i in range(l - 1, -1, -1):
            for j in range(i + 2, l):
                isPalindrome[i][j] = isPalindrome[i+1][j-1] and (s[i] == s[j])
                if isPalindrome[i][j] and j - i + 1 > longest:
                    longest = j - i + 1
                    start = i

        return s[start: start + longest]



print(Solution().longestPalindrome("abcddcbg"))

