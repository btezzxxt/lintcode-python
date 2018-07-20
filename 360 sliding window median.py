HashHeap = __import__("basic - hashheap").HashHeap
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        def addToHeap(maxHeap, minHeap, val):
            maxHeap.push(-val)
            if maxHeap.count - minHeap.count == 1 and minHeap.count != 0:
                if -maxHeap.peek() > minHeap.peek():
                    minHeap.push(-maxHeap.pop())
                    maxHeap.push(-minHeap.pop())
            elif maxHeap.count - minHeap.count > 1:
                minHeap.push(-maxHeap.pop())

        def delFromHeap(maxHeap, minHeap, val):
            if val <= -maxHeap.peek():
                maxHeap.delete(-val)
                if maxHeap.count < minHeap.count:
                    maxHeap.push(-minHeap.pop())
            else:
                minHeap.delete(val)
                if maxHeap.count - minHeap.count > 1:
                    minHeap.push(-maxHeap.pop())

        def getMedian(maxHeap, minHeap, k):
            return -maxHeap.peek()

        if len(nums) == 0 or len(nums) < k or k == 0:
            return []

        minHeap = HashHeap()
        maxHeap = HashHeap()

        res = []
        for j in range(k):
            addToHeap(maxHeap, minHeap, nums[j])       
        res.append(getMedian(maxHeap, minHeap, k))
        
        for i in range(k, len(nums)):
            addToHeap(maxHeap, minHeap, nums[i])
            delFromHeap(maxHeap, minHeap, nums[i-k])
            res.append(getMedian(maxHeap, minHeap, k))
        
        return res

print(Solution().medianSlidingWindow([1,2,7,7,2], 1))

            
