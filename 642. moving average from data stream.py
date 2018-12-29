from collections import deque
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque([])
        self.sum = 0
        self.max = size
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.queue.append(val)
        self.sum += val

        if len(self.queue) > self.max:
            left = self.queue.popleft()
            self.sum -= left
        
        return self.sum / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)