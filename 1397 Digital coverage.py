"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        timelines = []
        
        for interval in intervals:
            timelines.append((interval.start, 1))
            timelines.append((interval.end, 2))
        
        timelines.sort()
        
        max_cover = 0
        max_cover_val = -1 
        cover = 0
        
        for time, event in timelines:
            if event == 1:
                cover += 1 
                if cover > max_cover:
                    max_cover = cover 
                    max_cover_val = time 
            else:
                cover -= 1 
        return max_cover_val
                
                
# 扫描线