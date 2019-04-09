class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        hashmap = {}
        for word in words:
            if word in hashmap:
                hashmap[word] += 1 
            else:
                hashmap[word] = 1 
            
        arr = []    
        for key, value in hashmap.items():
            arr.append((value, key))
            
        arr.sort(key=lambda x: (-x[0], x[1]))
        
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res