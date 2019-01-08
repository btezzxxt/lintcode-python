"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        p1 = 0
        p2 = 0 
        res = []
        while p1 < len(list1) and p2 < len(list2):
            if list1[p1].start < list2[p2].start:
                self.push_result(res, list1[p1])
                p1 += 1
            else:
                self.push_result(res, list2[p2])
                p2 += 1
        
        while p1 < len(list1):
            self.push_result(res, list1[p1])
            p1 += 1
        
        while p2 < len(list2):
            self.push_result(res, list2[p2])
            p2 += 1
        
        return res
    
    def push_result(self, res, item):
        if not res:
            res.append(item)
            return
        
        last = res[-1]
        if last.end >= item.start:
            last.end = max(last.end, item.end)
        else:
            res.append(item)
        

