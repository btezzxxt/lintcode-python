class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        mirror_num = {
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
            '0': '0',
            '2': '5',
            '5': '2'
        }

        if not num:
            return False

        l = 0 
        r = len(num) - 1

        while l < r:
            num_l = num[l]
            num_r = num[r]
            if num_l not in mirror_num or mirror_num[num_l] != num_r:
                return False 
            l += 1 
            r -= 1

        if l == r:
            if num[l] not in "081":
                return False
        return True