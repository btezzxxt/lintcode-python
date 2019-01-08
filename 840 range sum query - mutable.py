class NumArray(object):
    # 回头再练习一下线段树的解法
    # binary index tree:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.bit = [0 for i in range(len(nums) + 1)]
        self.arr = [0 for i in range(len(nums))]

        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[i] 
        self.arr[i] = val

        ith = i + 1
        while ith < len(self.bit):
            self.bit[ith] += delta
            ith += self.lastBitOne(ith)


    def getSumOneTo(self, j):
        jth = j + 1
        sum = 0
        while jth != 0:
            sum += self.bit[jth]
            jth -= self.lastBitOne(jth)

        return sum
    
    def lastBitOne(self, x):
        return x & -x

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.getSumOneTo(j) - self.getSumOneTo(i - 1)
        return sum

a = NumArray([0,9,5,7,3])
print(a.bit)
print(a.sumRange(4, 4))
print(a.sumRange(2, 4))
print(a.sumRange(3, 3))
print(a.update(4, 5))
print(a.update(1, 7))
print(a.update(0, 8))
print(a.sumRange(1, 2))
print(a.update(1, 9))
print(a.sumRange(4, 4))
print(a.update(3, 4))
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
