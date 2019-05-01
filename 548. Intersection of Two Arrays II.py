class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        hashset = {}
        for num in nums1:
            if num not in hashset:
                hashset[num] = 1 
            else:
                hashset[num] += 1 

        res = []
        for num in nums2:
            if num in hashset:
                res.append(num)
                hashset[num] -= 1 
                if hashset[num] == 0:
                    del hashset[num]
        return res

print(Solution().intersection(num1, num2))
        