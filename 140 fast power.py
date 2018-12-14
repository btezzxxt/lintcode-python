# https://www.lintcode.com/problem/fast-power/description?_from=ladder&&fromId=1
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        div = a % b
        return self.powerHelper(div, b, n) % b

    def powerHelper(self, a, b, n):
        if n == 0:
            return 1

        half = self.powerHelper(a, b, n // 2) % b
        if n % 2 == 0:
            return (half * half)
        else:
            return (half * half * a)

print(Solution().fastPower(3,1,0))