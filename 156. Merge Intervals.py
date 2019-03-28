"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        res = []

        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            self.add(res, interval)
        return res 
        
    def add(self, res, interval):
        if not res:
            res.append(interval)
        
        last = res[-1]
        if last.end < interval.start:
            res.append(interval)
        else:
            res[-1] = Interval(last.start, max(last.end, interval.end))
            

        
            