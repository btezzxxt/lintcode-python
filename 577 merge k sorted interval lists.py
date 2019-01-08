"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop, heappush
from itertools import count
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        heap = []
        res = []
        incre_count = count()

        for interval in intervals:
            if not interval:
                continue
            item = interval[0]
            heappush(heap, (item.start, next(incre_count), item, interval, 0))
        
        while heap:
            _, _, item, interval, index = heappop(heap)
            self.result_push(res, item)
            if index + 1 < len(interval):
                next_item = interval[index + 1]
                heappush(heap, (next_item.start, next(incre_count), next_item, interval, index + 1))
        
        return res

    def result_push(self, res, item):
        if len(res) == 0:
            res.append(item)
            return
        
        prev = res[-1]
        if prev.end >= item.start:
            prev.end = max(prev.end, item.end)
        else:
            res.append(item)
            