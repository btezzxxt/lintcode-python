class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if not intervals:
            return [newInterval]
        
        index = -2
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval.start > newInterval.start:
                index = i - 1 
                break

        if index == -1:
            res = [newInterval]
            for i in range(len(intervals)):
                self.add(res, intervals[i])            
        elif index == -2:
            res = intervals
            self.add(res, newInterval)
        else:
            res = intervals[: index + 1]
            self.add(res, newInterval)
            for i in range(index + 1, len(intervals)):
                self.add(res, intervals[i])
            
        return res 
        
    def add(self, arr, interval):
        last = arr[-1]
        if last.end < interval.start:
            arr.append(interval)
        else:
            last.end = max(last.end, interval.end)
    
    