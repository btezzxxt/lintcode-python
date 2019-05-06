# class Solution:
#     """
#     @param: envelopes: a number of envelopes with widths and heights
#     @return: the maximum number of envelopes
#     """
#     def maxEnvelopes(self, envelopes):
#         # write your code here
#         envelopes.sort()
#         n = len(envelopes)
        
#         dp = [1] * n 
        
#         for i in range(1, n):
#             for j in range(0, i):
#                 if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)


import sys
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        n = len(envelopes)
        
        dp = [(sys.maxsize, sys.maxsize)] * (n + 1)
        dp[0] = (-sys.maxsize, -sys.maxsize)

        for i in range(n):
            index = self.bs_find_pos(dp, envelopes[i])
            if envelopes[i][1] < dp[index][1]:
                dp[index] = envelopes[i]
        
        for i in range(n, 0, -1):
            if dp[i] != (sys.maxsize, sys.maxsize):
                return i
        return 0

    def bs_find_pos(self, arr, envelope):
        w, h = envelope
        l = 0
        r = len(arr) - 1 
        while l + 1 < r:
            m = (l + r) // 2 
            if arr[m][0] < w and arr[m][1] < h:
                l = m 
            else:
                r = m 
        
        if arr[r][0] < w and arr[r][1] < h:
            return r + 1 
        elif arr[l][0] < w and arr[l][1] < h:
            return l + 1 
        else:
            return -1
        
# class Solution:
#     # @param {int[][]} envelopes a number of envelopes with widths and heights
#     # @return {int} the maximum number of envelopes
#     def maxEnvelopes(self, envelopes):
#         # Write your code here
#         height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
#         dp, length = [0] * len(height), 0

#         import bisect
#         for h in height:
#             i = bisect.bisect_left(dp, h, 0, length)
#             dp[i] = h
#             if i == length:
#                 length += 1
#         return length

print(Solution().maxEnvelopes([[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]))