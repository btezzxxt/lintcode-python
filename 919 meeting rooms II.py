class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        line = []
        for interval in intervals:
            # 把end排序的时候放前面 就可以先减后加 max不受影响
            line.append((interval.start, 1))
            line.append((interval.end, 0))
        room = 0
        max_ = 0
        line.sort()
        for point in line:
            if point[1] == 1:
                room += 1
            
            if point[1] == 0:
                room -= 1
            
            if room > max_:
                max_ = room
        return max_