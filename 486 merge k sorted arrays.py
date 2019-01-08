from heapq import heappop, heappush
from itertools import count
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        heap = []
        counter = count()
        res = []

        for array in arrays:
            if not array:
                continue
            heappush(heap, (array[0], next(counter), array, 0))
        
        while heap:
            value, _, array, index = heappop(heap)
            res.append(value)
            if index < len(array) - 1:
                heappush(heap, (array[index + 1], next(counter), array, index + 1))

        return res