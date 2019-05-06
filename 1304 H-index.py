class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def hIndex(self, citations):
        # write your code here
        
        l = 0 
        r = len(citations)
        
        while l + 1 < r:
            h = (l + r) // 2 
            if self.count_valid_citations(h, citations) >= h:
                l = h 
            else:
                r = h 
        
        if self.count_valid_citations(r, citations) >= r:
            return r 
        
        if self.count_valid_citations(l, citations) >= l:
            return l 
        return 0 
    
    def count_valid_citations(self, h, citations):
        count = 0 
        for cite in citations:
            if cite >= h:
                count += 1 
        return count 
        
        