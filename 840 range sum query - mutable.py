# class NumArray(object):
#     # 回头再练习一下线段树的解法
#     # binary index tree:
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.bit = [0 for i in range(len(nums) + 1)]
#         self.arr = [0 for i in range(len(nums))]

#         for i, num in enumerate(nums):
#             self.update(i, num)

#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: void
#         """
#         delta = val - self.arr[i] 
#         self.arr[i] = val

#         ith = i + 1
#         while ith < len(self.bit):
#             self.bit[ith] += delta
#             ith += self.lastBitOne(ith)


#     def getSumOneTo(self, j):
#         jth = j + 1
#         sum = 0
#         while jth != 0:
#             sum += self.bit[jth]
#             jth -= self.lastBitOne(jth)

#         return sum
    
#     def lastBitOne(self, x):
#         return x & -x

#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         sum = self.getSumOneTo(j) - self.getSumOneTo(i - 1)
#         return sum

# a = NumArray([0,9,5,7,3])
# print(a.bit)
# print(a.sumRange(4, 4))
# print(a.sumRange(2, 4))
# print(a.sumRange(3, 3))
# print(a.update(4, 5))
# print(a.update(1, 7))
# print(a.update(0, 8))
# print(a.sumRange(1, 2))
# print(a.update(1, 9))
# print(a.sumRange(4, 4))
# print(a.update(3, 4))
# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(i,val)
# # param_2 = obj.sumRange(i,j)

class Node():
    def __init__(self, val, start, end):
        self.val = val
        self.sum = 0
        self.start = start
        self.end = end


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.build(nums, 0, len(nums) - 1)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.update_helper(i, val, self.root)
    
    def update_helper(self, i, val, root):
        if not root:
            return 0
        
        mid = (root.start + root.end) // 2
        if mid == i:
            root.val = val
            root.sum = (root.left.sum if root.left else 0) + root.val + (root.right.sum if root.right else 0)
        elif i < mid:
            leftsum = self.update_helper(i, val, root.left)
            root.sum = leftsum + root.val + (root.right.sum if root.right else 0)
        else:
            rightsum = self.update_helper(i, val, root.right)
            root.sum = (root.left.sum if root.left else 0) + root.val + rightsum
        return root.sum
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_helper(i, j, self.root)
    
    def sum_helper(self, start, end, root):
        if start > end:
            return 0
        
        if root.start == start and root.end == end:
            return root.sum
        
        mid = (root.start + root.end) // 2
        if end < mid:
            res = self.sum_helper(start, end, root.left)
        elif start > mid:
            res = self.sum_helper(start, end, root.right)
        else:
            res = self.sum_helper(start, mid - 1, root.left) + root.val + self.sum_helper(mid + 1, end, root.right)

        return res


    def build(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = Node(nums[mid], start, end)
        root.left = self.build(nums, start, mid - 1)
        root.right = self.build(nums, mid + 1, end)

        root.sum = (root.left.sum if root.left else 0) + root.val + (root.right.sum if root.right else 0)
        return root
        



# Your NumArray object will be instantiated and called as such:
obj = NumArray([0,9,5,7,3])
obj.sumRange(4, 4)
obj.update(1, 2)
obj.sumRange(0, 2)