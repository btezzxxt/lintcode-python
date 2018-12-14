class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        minValIdx = self.searchMinIndex(A)
        idxA = self.binarySearch(A, 0, minValIdx - 1, target)
        idxB = self.binarySearch(A, minValIdx, len(A) - 1, target)
        
        if idxA == -1 and idxB == -1:
            return -1
        elif idxB != -1:
            return idxB
        elif idxA != -1:
            return idxA
        return -1

    def searchMinIndex(self, A):
        if len(A) == 0:
            return -1

        token = A[-1]
        left = 0
        right = len(A) - 1

        while left + 1 < right:
            mid = (left - right) // 2 + right
            if A[mid] < token:
                right = mid
            else:
                left = mid
        
        if A[right] > token and right + 1 < len(A):
            return right + 1
        elif A[left] > token and left + 1 < len(A):
            return left + 1
        else:
            return 0

    def binarySearch(self, A, start, end, target):
        if start > end:
            return -1
        
        if start >= len(A) or end < 0:
            return -1
        
        while start + 1 < end:
            mid = (start - end) // 2 + end
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        
        return -1

print(Solution().search([5], 5))