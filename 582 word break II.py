class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    # 用 divide and conquar 而不是traverse

    def wordBreak(self, s, wordDict):
        # write your code here
        res = []
        memo = {}
        res = self.dfs(s, wordDict, memo)
        return res

    # 返回s字符串所有valid的组合
    def dfs(self, s, wordDict, memo):
        if len(s) == 0:
            return []

        if s in memo:
            return memo[s]

        res = []
        for i in range(1, len(s) + 1):
            prefix = s[: i]
            if prefix in wordDict:
                sub = s[i:]
                substrings = self.dfs(sub, wordDict, memo)
                memo[sub] = substrings
                if len(substrings) > 0:
                    for i in range(len(substrings)):
                        res.append(prefix + ' ' + substrings[i])    
                else:
                    if len(sub) == 0:
                        res.append(prefix)
        return res

print(Solution().wordBreak("lintcode", ["de","ding","co","code","lint"]))