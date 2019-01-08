class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here

        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            while  p1 < len(nums1) and p2 < len(nums2) and nums1[p1] < nums2[p2]:
                p1 += 1

            while p1 < len(nums1) and p2 < len(nums2) and nums2[p2] < nums1[p1]:
                p2 += 1

            if p1 < len(nums1) and p2 < len(nums2) and nums1[p1] == nums2[p2]:
                if not res or (res and res[-1] != nums1[p1]):
                    res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res




        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        
        # set1 = set(nums1)

        # res = set()
        # for num in nums2:
        #     if num in set1:
        #         res.add(num)
        
        # return list(res)