class TrieNode:
    def __init__(self):
        self.children = {}
        self.has_word = False
        self.str = None
    
    @classmethod
    def addWord(cls, root, word):
        node = root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        
        node.has_word = True
        node.str = word


class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        # write your code here
        n = len(target)
        dp = [i for i in range(n + 1)]
        root = TrieNode()
        for word in words:
            TrieNode.addWord(root, word)
        
        res = []
        self.dfs(root, target, k, res, dp)      
        return res

    def dfs(self, node, target, k, res, dp):
        n = len(target)
        if node.has_word and dp[n] <= k:
            res.append(node.str)
        
        next_dp = [0 for _ in range(n + 1)]

        # 这步初始化是一个关键
        next_dp[0] = dp[0] + 1

        for next_letter, child_node in node.children.items():
            for i, target_letter in enumerate(target):
                seq = i + 1
                if next_letter == target_letter:
                    #3 cases cur match seq - 1, cur match seq and deletion of next + 1, next match seq - 1 and addition of seq char
                    next_dp[seq] = min(dp[seq - 1], dp[seq] + 1, next_dp[seq - 1] + 1)
                else:
                    next_dp[seq] = min(dp[seq - 1] + 1, dp[seq] + 1, next_dp[seq - 1] + 1)
            self.dfs(child_node, target, k, res, next_dp)

             
print(Solution().kDistance(["babbab"],"",1))
