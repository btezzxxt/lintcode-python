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

import sys
class Solution2:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if len(A) == 0:
            return []
        
        if len(A) < k:
            return []
        
        res = []
        index = self.get_biggest_result_smaller_eq(A, target)
        if index == -1:
            #表示找不到一个数小于等于target
            index = 0 #A[0] > target

        l = index 
        r = index + 1
        for i in range(k):
            left_diff, right_diff = sys.maxsize, sys.maxsize
            if l >= 0:
                left_diff = abs(A[l] - target)
            
            if r < len(A):
                right_diff = abs(A[r] - target)
                
            if left_diff <= right_diff:
                res.append(A[l])
                l -= 1
            else:
                res.append(A[r])
                r += 1
        return res
                
                

    
    def get_biggest_result_smaller_eq(self, A, target):
        l = 0
        r = len(A) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if A[m] > target:
                r = m 
            else:
                l = m 
        
        if A[r] <= target:
            return r
        
        if A[l] <= target:
            return l 
        
        return -1