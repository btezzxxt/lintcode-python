"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import OrderedDict
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        def addToMap(map, time, val):
            if time not in map:
                map[time] = val
            else:
                map[time] += val
        
        # write your code here
        if len(airplanes) == 0:
            return 0
        timeline = {}
        for ap in airplanes:
            addToMap(timeline, ap[0], 1)
            addToMap(timeline, ap[1], -1)
        
        arr = OrderedDict(sorted(timeline.items()))
        maxPlane = 0
        count = 0
        for key, val in arr.items():
            count += val
            maxPlane = max(maxPlane, count)

        return maxPlane
                
print(Solution().countOfAirplanes([(10,14),(10,15),(10,16),(1,10),(2,10),(3,10),(4,10)]))