# # recursion, a much better version
# class TrieNode:
#     def __init__(self):
#         self.hasEnd = False
#         self.children = {}


# class WordDictionary:
#     """
#     @param: word: Adds a word into the data structure.
#     @return: nothing
#     """
#     def __init__(self):
#         self.root = TrieNode()
        

#     def addWord(self, word):
#         # write your code here
#         cur = self.root
#         for letter in word:
#             if not letter in cur.children:
#                 cur.children[letter] = TrieNode()
#             cur = cur.children[letter]
#         cur.hasEnd = True

#     """
#     @param: word: A word could contain the dot character '.' to represent any one letter.
#     @return: if the word is in the data structure.
#     """
#     def search(self, word):
#         # write your code here
#         return self.searchInTrie(word, 0, self.root)

#     def searchInTrie(self, word, index, cur):
#         length = len(word)
#         if index == length:
#             return cur.hasEnd

#         for i in range(index, length):
#             letter = word[i]
#             if letter == ".":
#                 for child in cur.children.keys():
#                     if self.searchInTrie(word, i+1, cur.children[child]):
#                         return True
#                 return False
#             else:
#                 if letter in cur.children:
#                     return self.searchInTrie(word, i+1, cur.children[letter])        
#                 else:
#                     return False

# wd = WordDictionary()

# # wd.addWord("a")

# print(wd.search("."))
from collections import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.has_word = False

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        # write your code here
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.has_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search_iterate(self, word):
        # write your code here
        queue = deque([self.root])
        last_nodes = []
        for index, char in enumerate(word):             
            for _ in range(len(queue)):
                cur = queue.popleft()    
                if char not in cur.children and char != '.':
                    continue
                elif char in cur.children:
                    queue.append(cur.children[char])
                    if index == len(word) - 1:
                        last_nodes.append(cur.children[char])
                else:
                    queue.extend(cur.children.values())    
                    if index == len(word) - 1:
                        last_nodes.extend(cur.children.values())        

        for node in last_nodes:
            if node.has_word:
                return True

        return False

    def search(self, word):
        return self.search_recursive(word, 0, self.root)
        
    
    def search_recursive(self, word, index, trienode):
        if index == len(word):
            return trienode.has_word

        for i in range(index, len(word)):
            char = word[i]
            if char != '.':
                if char not in trienode.children:
                    return False
                else:
                    return self.search_recursive(word, index + 1, trienode.children[char])
            else:
                if len(trienode.children) == 0:
                    return False
                else:
                    for node in trienode.children.values():
                        if self.search_recursive(word, index + 1, node):
                            return True
                    return False

        
