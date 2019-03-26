# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.hasWord = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def addWord(self, word):
#         cur = self.root
#         for letter in word:
#             if not letter in cur.children:
#                 cur.children[letter] = TrieNode()
#             cur = cur.children[letter]
#         cur.hasWord = True

# class Solution:
#     """
#     @param board: A list of lists of character
#     @param words: A list of string
#     @return: A list of string
#     """
#     def wordSearchII(self, board, words):
#         # write your code here

#         if len(board) == 0 or len(board[0]) == 0:
#             return []
        
#         if len(words) == 0:
#             return []

#         trie = Trie()
#         res = set()

#         for word in words:
#             trie.addWord(word)
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.search(board, i, j, trie.root, res, "")
        
#         return list(res)

#     def search(self, board, i, j, trie, res, word):
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
#             return
        
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, 1, -1]

#         curLetter = board[i][j]
#         board[i][j] = '#'
#         curTrie = trie

#         if not curLetter in curTrie.children:
#             board[i][j] = curLetter
#             return
#         else:
#             word += curLetter
#             curTrie = curTrie.children[curLetter]
#             if curTrie.hasWord and word not in res:
#                 res.add(word)
            
#             for k in range(4):
#                 newI = i + dx[k]
#                 newJ = j + dy[k]
#                 self.search(board, newI, newJ, curTrie, res, word)
#         board[i][j] = curLetter
#         return


# board = ["abce","sfcs","adee"]

# for i in range(len(board)):
#     board[i] = list(board[i])

# print(Solution().wordSearchII(board, ["abcb","ninechapter","lintcode"]))

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.wordend = False

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]

        cur.wordend = True
    
    def has_prefix(self, word):
        cur = self.root 
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children
        
        return not cur.wordend
    
    def has_word(self, word):
        cur = self.root 
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children
        
        return cur.wordend

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        trie = Trie()
        for word in words:
            trie.add(word)

        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs_search(trie.root, board, i, j, [board[i][j]], res, {(i, j): True})
        return list(res)

    def dfs_search(self, trie_node, board, i, j, word, res, used):
        cur_val = board[i][j]
        
        if cur_val not in trie_node.children:
            return 
        elif trie_node.children[cur_val].wordend:           
            res.add("".join(word))       
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for k in range(4):
            di = i + dx[k]
            dj = j + dy[k]
            if 0 <= di and di < len(board) and 0 <= dj and dj < len(board[0]) and (di, dj) not in used:
                word.append(board[di][dj])
                used[(di, dj)] = True
                self.dfs_search(trie_node.children[cur_val], board, di, dj, word, res, used)
                word.pop()
                del used[(di, dj)]


board = ["doaf","agai","dcan"]

for i in range(len(board)):
    board[i] = list(board[i])

print(Solution().wordSearchII(board, ["dog","dad","dgdg","can","again"]))