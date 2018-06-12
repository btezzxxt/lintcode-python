# class Solution:
#     """
#     @param s: a string
#     @return: an integer
#     """
#     def lengthOfLongestSubstring(self, s):
#         # write your code here
#         i = 0
#         j = 0
#         map = {}
#         len1 = len(s)
#         count = 0
#         max_c = 0
#         for i, val in enumerate(s):
#             map[val] = True
#             count += 1
#             max_c = max(max_c, count)
#             while i+1 < len1 and (s[i+1] in map and map[s[i+1]]):
#                 map[s[j]] = False
#                 count -= 1
#                 j += 1
#             i += 1
#         return max_c

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        map = {}
        max_c = 0
        j = 0
        for i, v_back in enumerate(s):
            while j < len(s):
                if s[j] not in map or map[s[j]] == False:
                    map[s[j]] = True
                    max_c = max(max_c, j - i + 1)
                    j += 1
                else:
                    break
            map[v_back] = False
        return max_c

print(Solution().lengthOfLongestSubstring("an++--viaj"))