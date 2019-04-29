"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example
Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: "horse", "ros"
Output: 4
Explanation: You need three steps to make "horse" to "os" and another step to make "ros" to "os".
Notice
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""

class Solution2:
    """
    @param word1: a string
    @param word2: a string
    @return: return a integer
    """
    def minDistance(self, word1, word2):
        # write your code here
        l1 = len(word1)
        l2 = len(word2)

        dp = [[0 for i in range(l1 + 1)] for i in range(l2 + 1)]

        for i in range(l2 + 1):
            dp[i][0] = i 
        
        for j in range(l1 + 1):
            dp[0][j] = j 
        
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1) # dp[i - 1][j - 1] <= dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1) # dp[i - 1][j - 1] + 2 >= the other two
        return dp[l2][l1]

class Solution:
    """
    @param word1: a string
    @param word2: a string
    @return: return a integer
    """
    def minDistance(self, word1, word2):
        # write your code here
        l1 = len(word1)
        l2 = len(word2)

        dp = [[0 for i in range(l1 + 1)] for i in range(2)]

        
        for j in range(l1 + 1):
            dp[0][j] = j 
        
        for i in range(1, l2 + 1):
            for j in range(0, l1 + 1):
                if j == 0:
                    dp[i % 2][j] = i 
                    continue

                if word2[i - 1] == word1[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1)
        return dp[l2 % 2][l1]