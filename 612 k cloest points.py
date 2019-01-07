class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Point2:
    def __init__(self, a, b, a0, b0):
        self.x = a
        self.y = b
        self.d = self._calculate_distance(a, b, a0, b0)

    def _calculate_distance(self, x, y, a, b):
        return (x -a) ** 2 + (y - b) ** 2
    
    # 重写less than的做法
    def __lt__(self, other):
        if self.d < other.d:
            return True

        if self.d == other.d and self.x < other.x:
            return True

        if self.d == other.d and self.x == self.x and self.y < other.y:
            return True
        
        return False

from heapq import heappush, heappop
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        heap = []
        for point in points:
            p = Point2(point.x, point.y, origin.x, origin.y)
            heappush(heap, p)
        res = []
        for _ in range(k):
            p = heappop(heap)
            res.append(Point(p.x, p.y))
        
        return res
