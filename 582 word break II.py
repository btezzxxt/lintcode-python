# class Solution:
#     """
#     @param: s: A string
#     @param: wordDict: A set of words.
#     @return: All possible sentences.
#     """
#     # 用 divide and conquar 而不是traverse

#     def wordBreak(self, s, wordDict):
#         # write your code here
#         res = []
#         memo = {}
#         res = self.dfs(s, wordDict, memo)
#         return res

#     # 返回s字符串所有valid的组合
#     def dfs(self, s, wordDict, memo):
#         if len(s) == 0:
#             return []

#         if s in memo:
#             return memo[s]

#         res = []
#         for i in range(1, len(s) + 1):
#             prefix = s[: i]
#             if prefix in wordDict:
#                 sub = s[i:]
#                 substrings = self.dfs(sub, wordDict, memo)
#                 memo[sub] = substrings
#                 if len(substrings) > 0:
#                     for i in range(len(substrings)):
#                         res.append(prefix + ' ' + substrings[i])    
#                 else:
#                     if len(sub) == 0:
#                         res.append(prefix)
#         return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.has_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.has_word = True
    
    def find(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.has_word
        
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        res = []
        wordset = set()
        trie = Trie()
        for word in wordDict:
            trie.add(word)
            
        memo = {}
        res = self.dfs(s, trie, memo)
        return res 
        
    # def dfs(self, s, start, trie, path, res):
    #     if start == len(s):
    #         res.append(" ".join(path))
    #         return res 
        
    #     for i in range(start, len(s)):
    #         curword = s[start: i + 1]
    #         if not trie.find(curword):
    #             continue
    #         path.append(curword)
    #         self.dfs(s, i + 1, trie, path, res)
    #         path.pop()
    
    def dfs(self, cur_str, trie, memo):
        if cur_str == "":
            return [""]
            
        if cur_str in memo:
            return memo[cur_str]
        
        res = []
        for i in range(0, len(cur_str)):
            word = cur_str[0: i + 1]
            if trie.find(word):
                next_res = self.dfs(cur_str[i + 1:], trie, memo)
                for string in next_res:
                    if string:
                        res.append(word + " " + string)
                    else:
                        res.append(word)

                    
        memo[cur_str] = res
        return res 
                    
        
# 二叉树版本
print(Solution().wordBreak("lintcode", ["de","ding","co","code","lint"]))