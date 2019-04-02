from heapq import heappop, heappush
class Solution:

    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = []
        heappush(heap, 1)
        visited = set()
        
        count = 0
        while heap:
            cur = heappop(heap)
            count += 1
            if count == n:
                return cur
            for mul in [2,3,5]:
                temp = cur * mul
                if temp not in visited:
                    heappush(heap, temp)
                    visited.add(temp)
        return -1
