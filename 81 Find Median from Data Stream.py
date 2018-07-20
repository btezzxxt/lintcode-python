# HashHeap = __import__('basic - HashHeap.py')
from heapq import heappop, heappush
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if len(nums == 0):
            return []
        maxHeap = []
        minHeap = []

        def addToHeap(maxHeap, minHeap, val):
            heappush(maxHeap, -val)
            if len(maxHeap) - len(minHeap) == 1:
                if -maxHeap[0] > minHeap[0]:
                    heappush(maxHeap, -heappop(minHeap))
                    heappush(minHeap, -heappop(maxHeap))
            elif len(maxHeap) - len(minHeap) > 1:
                heappush(minHeap, -heappop(maxHeap))

        def getMedian(maxHeap, minHeap):
            return -maxHeap[0]

        res = []
        for i in range(len(nums)):
            addToHeap(maxHeap, minHeap, nums[i])
            res.append(getMedian(maxHeap, minHeap))
        return res