from random import randint

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        def patition(arr, l, r):
            ri = randint(l, r)
            arr[l], arr[ri] = arr[ri], arr[l]
            
            pivot = arr[l]
            while l < r:
                while l < r and arr[r] >= pivot:
                    r -= 1
                arr[l] = arr[r]
                while l < r and arr[l] <= pivot:
                    l += 1    
                arr[r] = arr[l]
            arr[l] = pivot
            return l

        def quickSelect(arr, l, r, k):
            if l == r:
                return arr[l]

            pi = patition(arr, l, r)
            if pi == k:
                return arr[pi]
            elif pi < k:
                return quickSelect(arr, pi + 1, r, k)
            else:
                return quickSelect(arr, l, pi - 1, k)                 

        
        return quickSelect(nums, 0, len(nums)-1, k -1)