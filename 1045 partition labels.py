class Solution:
    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """
    def partitionLabels(self, S):
        # Write your code here
        letter_pos = {}
        
        # kind of, similar to max swap integer, use a map to save last apearance index of letter
        # use a left point to save part start, update right bounder with max(right, map[char])
        # when i == right, this part is done, add length to res, update left to (right + 1)
        
        for i, letter in enumerate(S):
            letter_pos[letter] = i 
        
        res = []
        left = 0 
        right = 0
        for i in range(len(S)):
            letter = S[i]
            right = max(right, letter_pos[letter])
            
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res            
            
            