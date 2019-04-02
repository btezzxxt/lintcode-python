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

# class TrieNode:
#     def __init__(self, val):
#         self.val = val
#         self.children = {}
#         self.wordend = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode(None)
    
#     def add(self, word):
#         cur = self.root
#         for char in word:
#             if char not in cur.children:
#                 cur.children[char] = TrieNode(char)
#             cur = cur.children[char]

#         cur.wordend = True
    
#     def has_prefix(self, word):
#         cur = self.root 
#         for char in word:
#             if char not in cur.children:
#                 return False
#             else:
#                 cur = cur.children
        
#         return not cur.wordend
    
#     def has_word(self, word):
#         cur = self.root 
#         for char in word:
#             if char not in cur.children:
#                 return False
#             else:
#                 cur = cur.children
        
#         return cur.wordend

# class Solution:
#     """
#     @param board: A list of lists of character
#     @param words: A list of string
#     @return: A list of string
#     """
#     def wordSearchII(self, board, words):
#         # write your code here
#         trie = Trie()
#         for word in words:
#             trie.add(word)

#         res = set()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.dfs_search(trie.root, board, i, j, [board[i][j]], res, {(i, j): True})
#         return list(res)

#     def dfs_search(self, trie_node, board, i, j, word, res, used):
#         cur_val = board[i][j]
        
#         if cur_val not in trie_node.children:
#             return 
#         elif trie_node.children[cur_val].wordend:           
#             res.add("".join(word))       
        
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]

#         for k in range(4):
#             di = i + dx[k]
#             dj = j + dy[k]
#             if 0 <= di and di < len(board) and 0 <= dj and dj < len(board[0]) and (di, dj) not in used:
#                 word.append(board[di][dj])
#                 used[(di, dj)] = True
#                 self.dfs_search(trie_node.children[cur_val], board, di, dj, word, res, used)
#                 word.pop()
#                 del used[(di, dj)]


# board = ["doaf","agai","dcan"]

# for i in range(len(board)):
#     board[i] = list(board[i])

# print(Solution().wordSearchII(board, ["dog","dad","dgdg","can","again"]))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.has_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.has_end = True
    
    def find(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


class Solution:
    def wordSearchII(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self._dfs(i, j, board, trie.root, [board[i][j]], res, set([(i, j)]))
        return list(res)

    def _dfs(self, i, j, board, trie, path, res, visited):
        char = board[i][j]
        if char not in trie.children:
            return
        elif trie.children[char].has_end:
            res.add("".join(path))
            

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for k in range(4):
            i_new = i + dx[k]
            j_new = j + dy[k]
            if self._is_valid_pos(board, i_new, j_new) and (i_new, j_new) not in visited:
                nxt_char = board[i_new][j_new]
                path.append(nxt_char)
                visited.add((i_new, j_new))
                self._dfs(i_new, j_new, board, trie.children[char], path, res, visited)
                path.pop()
                visited.remove((i_new, j_new))

    def _is_valid_pos(self, board, i, j):
        m = len(board)
        n = len(board[0])

        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False
board = ["doaf","agai","dcan"]

for i in range(len(board)):
    board[i] = list(board[i])

print(Solution().wordSearchII(board, ["dog","dad","dgdg","can","again"]))