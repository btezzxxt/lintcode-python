from heapq import heappop, heappush
class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        if len(arrays) == 0:
            return -1
        maxheap = []
        for array in arrays:
            for item in array:
                heappush(maxheap, 0-item)
        res = -1
        for i in range(k):
            res = heappop(maxheap)
        
        return -res