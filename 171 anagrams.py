import collections
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        hashmap = collections.defaultdict(list)
        for word in strs:
            id = self.get_id(word)
            hashmap[id].append(word)
        
        res = []
        for words in hashmap.values():
            if len(words) >= 2:
                res.extend(words)
        return res
    
    def get_id(self, word):
        letters = [0] * 26 
        for char in word:
            letters[ord(char) - ord('a')] += 1 
        id = 0
        for count in letters:
            id = id * 10 + count 
        return id 