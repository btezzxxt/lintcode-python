class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # kth biggest is len(nums) - k smallest + 1
        smallest = len(nums) - n + 1
        return self.partition(nums, 0, len(nums) - 1, smallest)
    # get kth smallest
    def partition(self, nums, l, r, k):
        if l == r:
            return nums[l]
        
        pivot = nums[l] 
        while l < r:
            while l < r and nums[r] > pivot:
                r = r - 1
            nums[l] = nums[r]
            while l < r and nums[l] < pivot:
                l = l + 1
            nums[r] = nums[l]
        nums[l] = pivot

        # l is the pivot location, l + 1 is the kth smallest
        if k == l + 1:
            return nums[l]
        elif k > l + 1:
            return self.partition(nums, l + 1, len(nums) - 1, k)
        else:
            return self.partition(nums, 0, l - 1, k) 

print(Solution().kthLargestElement(3, [9,3,2,4,8]))
