class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.root = {
            "children": {}
        }
        

    def addWord(self, word):
        # write your code here
        cur = self.root
        length = len(word)
        for i, letter in enumerate(word):
            if not letter in cur["children"]:
                cur["children"][letter] = { 
                    "hasEnd": True if i == length - 1 else False,
                    "children": {}
                }
            else:
                if i == length - 1:
                    cur["children"][letter]["hasEnd"] = True 
            cur = cur["children"][letter]

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.searchInTrie(word, self.root)

    def searchInTrie(self, word, trie):
        cur = trie
        length = len(word)
        for i, letter in enumerate(word):
            if letter == ".":
                found = False
                for child in cur["children"].keys():
                    if i == length - 1:
                        return True if cur["children"][child]["hasEnd"] else False
                    else:
                        found = found or self.searchInTrie(word[i+1:], cur["children"][child])
                return found
            else:
                if not letter in cur["children"]:
                    return False        
                else:
                    cur = cur["children"][letter]
                    if i == length - 1 and cur["hasEnd"]:
                        return True
        return False

wd = WordDictionary()
wd.addWord("ran")
wd.addWord("rune")
wd.addWord("runner")
wd.addWord("runs")
wd.addWord("add")
wd.addWord("adds")
wd.addWord("adder")
wd.addWord("addee")

print(wd.search("...s"))


