class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if k == 0:
            return []

        arr = []
        closestIndex = self.findClosestIndex(A, target)
        arr.append(A[closestIndex])
        k = k - 1

        nextIndex = closestIndex + 1
        preIndex = closestIndex - 1
        while k > 0:
            if nextIndex  < len(A) and preIndex >= 0:
                if abs(A[preIndex] - target) > abs(A[nextIndex] - target):
                    arr.append(A[nextIndex])
                    nextIndex = nextIndex + 1
                else:
                    arr.append(A[preIndex])
                    preIndex = preIndex - 1
            elif preIndex >=0:
                arr.append(A[preIndex])
                preIndex = preIndex - 1
            elif nextIndex < len(A):
                arr.append(A[nextIndex])
                nextIndex = nextIndex + 1
            k = k - 1
        return arr

        
    def findClosestIndex(self, A, target):
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left - right) // 2 + right 
            if A[mid] > target:
                right = mid
            else:
                left = mid
        
        if A[left] == target:
            return left
        
        elif A[right] == target:
            return right
        
        elif abs(A[left] - target) > abs(A[right] - target):
            return right
        else:
            return left

print(Solution().kClosestNumbers([1,4,6,8],3,3))

# binary search + two pointers