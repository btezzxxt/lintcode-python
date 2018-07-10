class TrieNode:
    def __init__(self):
        self.children = {}
        self.hasWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for letter in word:
            if not letter in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.hasWord = True

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here

        if len(board) == 0 or len(board[0]) == 0:
            return []
        
        if len(words) == 0:
            return []

        trie = Trie()
        res = set()

        for word in words:
            trie.addWord(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, trie.root, res, "")
        
        return list(res)

    def search(self, board, i, j, trie, res, word):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        curLetter = board[i][j]
        board[i][j] = '#'
        curTrie = trie

        if not curLetter in curTrie.children:
            board[i][j] = curLetter
            return
        else:
            word += curLetter
            curTrie = curTrie.children[curLetter]
            if curTrie.hasWord and word not in res:
                res.add(word)
            
            for k in range(4):
                newI = i + dx[k]
                newJ = j + dy[k]
                self.search(board, newI, newJ, curTrie, res, word)
        board[i][j] = curLetter
        return


board = ["abce","sfcs","adee"]

for i in range(len(board)):
    board[i] = list(board[i])

print(Solution().wordSearchII(board, ["abcb","ninechapter","lintcode"]))