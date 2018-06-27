# recursion, a much better version
class TrieNode:
    def __init__(self):
        self.hasEnd = False
        self.children = {}


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
        for letter in word:
            if not letter in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.hasEnd = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.searchInTrie(word, 0, self.root)

    def searchInTrie(self, word, index, cur):
        length = len(word)
        if index == length:
            return cur.hasEnd

        for i in range(index, length):
            letter = word[i]
            if letter == ".":
                for child in cur.children.keys():
                    if self.searchInTrie(word, i+1, cur.children[child]):
                        return True
                return False
            else:
                if letter in cur.children:
                    return self.searchInTrie(word, i+1, cur.children[letter])        
                else:
                    return False

wd = WordDictionary()

# wd.addWord("a")

print(wd.search("."))


