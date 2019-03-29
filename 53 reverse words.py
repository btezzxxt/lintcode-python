class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        # words = s.split(" ")
        # res = []
        # for i in range(len(words) - 1, -1 , -1):
        #     word = words[i].strip()
        #     if len(word) > 0:
        #         res.append(word)
        # return " ".join(res)
        
        words = s.split()
        words.reverse()
        return " ".join(words)