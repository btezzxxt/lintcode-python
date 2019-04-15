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


class Solution2:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        arr = self.mergesort(A, 0, len(A) - 1)
        for i in range(len(arr)):
            A[i] = arr[i]
    
    def mergesort(self, A, l, r):
        if l > r:
            return []
        
        if l == r:
            return [A[l]]
        
        mid = (l + r) // 2 
        arr1 = self.mergesort(A, l, mid)
        arr2 = self.mergesort(A, mid + 1, r)
        arr = self.merge(arr1, arr2)
        return arr
        
    def merge(self, arr1, arr2):
        if not arr1:
            return arr2
        
        if not arr2:
            return arr1
            
        p1, p2 = 0, 0
        
        res = [] 
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] <= arr2[p2]:
                res.append(arr1[p1])
                p1 += 1
            else:
                res.append(arr2[p2])
                p2 += 1 
            
        while p1 < len(arr1):
            res.append(arr1[p1])
            p1 += 1 
        
        while p2 < len(arr2):
            res.append(arr2[p2])
            p2 += 1 
        
        return res
        
    def sortIntegers2_star(self, A):
        # write your code here
        self.quicksort(A, 0, len(A) - 1)
        
    def quicksort(self, A, start, end):
        if start < end:
            lower, upper = self.partition(A, start, end)
            self.quicksort(A, start, lower)
            self.quicksort(A, upper, end)
    
    def partition(self, A, start, end):
        l = start
        r = end
        pivot = A[(start + end) // 2]
        
        while l <= r:
            while l <= r and A[r] > pivot:
                r -= 1 
            while l <= r and A[l] < pivot:
                l += 1 
            
            if l <= r:
                A[l], A[r] = A[r], A[l]
                l += 1 
                r -= 1 
        return r, l


print(Solution2().partition([3,1,3,1,3], 0, 4))