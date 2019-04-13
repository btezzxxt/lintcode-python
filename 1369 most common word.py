import re
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        count_map = {}
        regex = re.compile("\w+")
        words = regex.findall(paragraph.lower())
        for word in words:
            word = word
            if word not in banned:
                if word not in count_map:
                    count_map[word] = 1
                else:
                    count_map[word] += 1 

        arr = [(count, word) for word, count in count_map.items()]
        arr.sort(key=lambda x : -x[0])
        return arr[0][1]
        
        
