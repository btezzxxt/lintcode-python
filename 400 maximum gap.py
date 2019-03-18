import sys
import math

class Bucket:
    def __init__(self):
        self.min = sys.maxsize
        self.max = -sys.maxsize
        self.isEmpty = True

class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        # write your code here
        maxi = max(nums)
        mini = min(nums)
        leng = len(nums)
        avg_gap = (maxi - mini) / (leng - 1)

        #avg_gap ==0 表示所有数一样大 gap 为0
        if avg_gap == 0:
            return 0
        
        buckets = [Bucket() for _ in range(leng)]

        for num in nums:
            buck_seq = math.floor((num - mini) / avg_gap)
            counter = buckets[buck_seq]
            counter.isEmpty = False

            if counter.min > num:
                counter.min = num
                
            if counter.max < num:
                counter.max = num

        max_gap = 0
        start = 0
        # 找到第一个非空bucket
        for i in range(0, len(buckets)):
            if not buckets[i].isEmpty:
                start = i
                pre = buckets[i]
                break

        # 不断下个非空bucket和前一个比较cur.min - pre.max，找到最大的那个gap
        for i in range(start + 1, len(buckets)):
            if buckets[i].isEmpty:
                continue
            cur = buckets[i]

            if cur.min - pre.max > max_gap:
                max_gap = cur.min - pre.max
            pre = cur

        return max_gap