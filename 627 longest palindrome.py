# find longest palindrome
# class Solution:
#     """
#     @param s: a string which consists of lowercase or uppercase letters
#     @return: the length of the longest palindromes that can be built
#     """
#     def lengthOfPalindrome(self, s, i, j):
#         if i == j:
#             count = -1 
#         else:
#             count = 0
        
#         while i >= 0 and j < len(s) and s[i] == s[j]:
#             count = count + 2
#             i = i - 1 
#             j = j + 1
#         return count
    
#     def longestPalindrome(self, s):
#         # write your code here
#         max_ = 0
#         for i in range(len(s)):
#             max_ = max(max_, self.lengthOfPalindrome(s, i, i), self.lengthOfPalindrome(s, i, i + 1))
#         return max_

# print(Solution().longestPalindrome("abccccdd"))

# built the longest palindrome
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        map_ = {}
        for i in range(len(s)):
            if s[i] not in map_:
                map_[s[i]] = 1 
            else:
                map_[s[i]] = map_[s[i]] + 1 
        
        count = 0
        single_point = False
        for key in map_:
            if map_[key] % 2 == 0:
                count = count + map_[key]
            else:
                count = count + map_[key] - 1 
                single_point = True
            
        count = count + 1 if single_point else count 
        return count
        
print(Solution().longestPalindrome("abccccdd"))