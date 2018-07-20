class Solution:
    def sqrt(self, x):
        # write your code here
        l = 0
        r = x if x >= 1 else 1 # 难点1 max范围 如果 x > 1 那么m < x 如果 x 是小数， r应该 < 1
        eps = 1e-11
        while l < r:
            m = l - (l - r) / 2
            if m - x / m > -eps and m - x/m < eps:  # 判断 m 和 x/m的精度是不是 < 1e-11
                return m 
            elif m > x / m:
                r = m
            else:
                l = m
        return l