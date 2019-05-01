"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        
        cur = None
        for interval in intervals:
            if cur == None:
                cur = interval 
            else:
                if cur.end > interval.start:
                    return False 
                else:
                    cur = interval
        return True
        