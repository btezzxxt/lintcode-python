# class TrieNode:
#     def __init__(self):
#         self.hasWord = False
#         self.children = {}


# class Trie:
#     def __init__(self):
#         # do intialization if necessary
#         self.root = TrieNode()

#     """
#     @param: word: a word
#     @return: nothing
#     """
#     def insert(self, word):
#         # write your code here
#         cur = self.root
#         for letter in word:
#             if not letter in cur.children:
#                 cur.children[letter] = TrieNode()
#             cur = cur.children[letter]
#         cur.hasWord = True

#     """
#     @param: word: A string
#     @return: if the word is in the trie.
#     """
#     def search(self, word):
#         # write your code here
#         cur = self.root
#         for letter in word:
#             if not letter in cur.children:
#                 return False
#             else:
#                 cur = cur.children[letter]
#         return cur.hasWord

#     """
#     @param: prefix: A string
#     @return: if there is any word in the trie that starts with the given prefix.
#     """
#     def startsWith(self, prefix):
#         # write your code here
#         cur = self.root
#         for letter in prefix:
#             if not letter in cur.children:
#                 return False
#             else:
#                 cur = cur.children[letter]
#         return not cur.hasWord

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()
        
    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word_end = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word_end

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # not matter whether the word ends here, return True cause 'a' startsWith 'a' too
        return True
