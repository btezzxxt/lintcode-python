from heapq import heappop, heappush
class Solution:

    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = []
        visited = set([1])
        heappush(heap, 1)
        cur = -1
        for _ in range(n):
            cur = heappop(heap)
            for mul in [2, 3, 5]:
                new = cur * mul
                if new not in visited:
                    visited.add(new)
                    heappush(heap, new)
        return cur
