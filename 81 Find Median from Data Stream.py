# # HashHeap = __import__('basic - HashHeap.py')
# from heapq import heappop, heappush
# class Solution:
#     """
#     @param nums: A list of integers
#     @return: the median of numbers
#     """
#     def medianII(self, nums):
#         # write your code here
#         if len(nums == 0):
#             return []
#         maxHeap = []
#         minHeap = []

#         def addToHeap(maxHeap, minHeap, val):
#             heappush(maxHeap, -val)
#             if len(maxHeap) - len(minHeap) == 1:
#                 if -maxHeap[0] > minHeap[0]:
#                     heappush(maxHeap, -heappop(minHeap))
#                     heappush(minHeap, -heappop(maxHeap))
#             elif len(maxHeap) - len(minHeap) > 1:
#                 heappush(minHeap, -heappop(maxHeap))

#         def getMedian(maxHeap, minHeap):
#             return -maxHeap[0]

#         res = []
#         for i in range(len(nums)):
#             addToHeap(maxHeap, minHeap, nums[i])
#             res.append(getMedian(maxHeap, minHeap))
#         return res

from heapq import heappop, heappush
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if len(nums) == 0:
            return []
        max_h = []
        min_h = []
        
        res = []
        for num in nums:
            if not max_h:
                heappush(max_h, -num)
                res.append(-max_h[0])
            else:
                median = -max_h[0]
                if num > median:
                    heappush(min_h, num)
                    self.balance(max_h, min_h)
                else:
                    heappush(max_h, -num)
                    self.balance(max_h, min_h)
                res.append(-max_h[0])
        return res 
    
    def balance(self, max_heap, min_heap):
        len1 = len(max_heap)
        len2 = len(min_heap)
        if len1 == len2:
            return 
        elif len1 - len2 == 1:
            return 
        elif len1 > len2:
            val = -heappop(max_heap)
            heappush(min_heap, val)
        else:
            val = heappop(min_heap)
            heappush(max_heap, -val)

