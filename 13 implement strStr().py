class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source == "" and target == "":
            return 0 

        for i in range(len(source)):
            if self.match(source, i, target):
                return i
        return -1
        
    def match(self, source, start, target):
        if len(source) - start < len(target):
            return False
        
        for i in range(len(target)):
            if target[i] != source[start + i]:
                return False
        
        return True
