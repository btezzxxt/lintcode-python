# class Solution:
#     """
#     @param str: s string
#     @return: return an integer, denote the number of the palindromic substrings
#     """
#     # O(n ^ 3) LTE
#     def countPalindromicSubstrings(self, str):
#         # write your code here
#         if not str:
#             return 0 
        
#         count = 0
#         for i in range(len(str)):
#             for j in range(i, len(str)):
#                 if self.is_palindrome(str, i, j):
#                     count += 1 
#         return count 
        
#     def is_palindrome(self, str, i, j):
#         if i == j:
#             return True 
        
#         while i < j:
#             if str[i] != str[j]:
#                 return False 
            
#             i += 1 
#             j -= 1 
#         return True

class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, str):
        # write your code here
        if not str:
            return 0 
        
        n = len(str)
        dp = [[False for i in range(n)] for i in range(n)]
        
        count = 0
        for j in range(1, n + 1):
            for i in range(n):
                k = i + j - 1 
                if k >= n:
                    break

                if i == k:
                    dp[i][k] = True
                    count += 1 
                elif i + 1 == k:
                    if str[i] == str[k]:
                        dp[i][k] = True 
                        count += 1
                else:
                    if str[i] == str[k] and dp[i + 1][k - 1]:
                        dp[i][k] = True 
                        count += 1 
        return count 

print(Solution().countPalindromicSubstrings("aaaa"))