class TrieNode:
    def __init__(self):
        self.hasWord = False
        self.children = {}


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
        for letter in word:
            if not letter in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.hasWord = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        cur = self.root
        for letter in word:
            if not letter in cur.children:
                return False
            else:
                cur = cur.children[letter]
        return cur.hasWord

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        cur = self.root
        for letter in prefix:
            if not letter in cur.children:
                return False
            else:
                cur = cur.children[letter]
        return not cur.hasWord