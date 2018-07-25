class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        def canCut(woods, m, k):
            total = 0
            for wood in woods:
                total += wood // m
            return total >= k
        if len(L) == 0:
            return 0

        max_ = max(L)
        l = 0
        r = max_
        while l + 1 < r:
            m = l + (r - l) // 2
            if canCut(L, m, k):
                l = m
            else:
                r = m
        if canCut(L, r, k):
            return r
        return l