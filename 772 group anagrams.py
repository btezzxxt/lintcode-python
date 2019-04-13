class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        count_map = {}
        for word in strs:
            converted = self.convert(word)
            count_map[converted] = count_map.get(converted, [])
            count_map[converted].append(word)
        return count_map.values()
    
    def convert(self, word):
        letters = [0] * 26
        for letter in word:
            num = ord(letter) - ord("a")
            letters[num] += 1 
        
        id = 0
        for num in letters:
            id = id * 10 + num 
        return id 