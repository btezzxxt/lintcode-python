class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        if not words or not words[0]:
            return True 
            
        if len(words) != len(words[0]):
            return False
            
        n = len(words)
        for i in range(n):
            for row in range(n):
                if words[row][i] != words[i][row]:
                    return False 
        return True