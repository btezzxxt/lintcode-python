class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        # 一开始用倍增法法来找包含target的右边界
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1
        
        left, right = 0, index
        while left + 1 < right:
            mid = (left - right) // 2 + right
            # 即使找到了target依然right=mid 因为这道题要找到最小的那个target
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid
        
        if reader.get(left) == target:
            return left
        elif reader.get(right) == target:
            return right
        return -1