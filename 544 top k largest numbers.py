from heapq import heappop, heappush
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        heap = []
        for num in nums:
            heappush(heap, -num)
        
        res = []
        for _ in range(k):
            res.append(-heappop(heap))

        return res