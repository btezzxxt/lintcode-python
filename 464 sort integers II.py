from random import randint
from heapq import heappush
from heapq import heappop
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        # self.quickSort(0, len(A) - 1, A)
        # self.heapSort(A)
        return self.mergeSort(A)

    def mergeSort(self, A):
        A = self.mergeSortHelper(A, 0, len(A) - 1)
        return A

    def mergeSortHelper(self, A, start, end):
        if start < end:
            mid = (start - end) // 2 + end
            arrl = self.mergeSortHelper(A, start, mid)
            arrr = self.mergeSortHelper(A, mid + 1, end)
            return self.mergeTwoArr(arrl, arrr)
        else:
            return A[start: end + 1]

    def mergeTwoArr(self, arrl, arrr):
        arr = []
        
        l, r = 0, 0
        while l < len(arrl) and r < len(arrr):
            if arrl[l] < arrr[r]:
                arr.append(arrl[l])
                l = l + 1
            else:
                arr.append(arrr[r])
                r = r + 1
        while l < len(arrl):
            arr.append(arrl[l])
            l = l + 1
        while r < len(arrr):
            arr.append(arrr[r])
            r = r + 1
        return arr
            

    def heapSort(self, A):
        heap = []
        for num in A:
            heappush(heap, num)
        
        for i in range(len(A)):
            A[i] = heappop(heap)
        return

    def quickSort(self, start, end, A):
        if start < end:
            idx = self.partition(start, end, A)
            self.quickSort(start, idx - 1, A)
            self.quickSort(idx + 1, end, A)


    # Quick sort
    def partition(self, start, end, A):
        random = randint(start, end)
        A[start], A[random] = A[random], A[start]

        # pivot 不是index 永远是那个值 return 的是start
        # pivot拿走 留下第一个坑
        pivot = A[start]
        while start < end:
            # 从右边开始 找一个小于pivot的 放到左边的坑里
            while start < end and A[end] >= pivot:
                end = end - 1
            A[start] = A[end]
            # 经过上一步 右边有个坑 左边指针找个大于pivot的数 填坑 挖一个左边的坑
            while start < end and A[start] <= pivot:
                start = start + 1
            A[end] = A[start]
            
            #下一个循环 重复   
        # 左右指针相遇，说明左边没有比pivot值小的了，右边也没有比pivot大的了， 把pivot填入最后一个坑
        A[start] = pivot

        # 坑的位置刚好是start
        return start


    # merge sort
    
    # heap sort

print(Solution().sortIntegers2([3,2,1,4,5]))
