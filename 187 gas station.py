class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        remain = 0
        total = 0
        start = 0

        for i in range(len(gas)):
            remain = remain + gas[i] -cost[i]
            total = total + gas[i] - cost[i]
            if remain < 0:
                start = i + 1
                remain = 0

        if total >= 0:
            return start
        return -1
            

# 证明： 如果total > 0 则必定存在一点i，当从i起始可以走完全程

# 证明办法：先在全程上找到使得total(i, j) 最大的两点。下面假设存在有一点m，使得total（i,m）< 0。因为total>0，total（i,m）< 0 所以total（m+1，i-1）一定>0。
#          那么我们就得到total(m+1, j) > total(i, j)，这个结论与已知total(i, j)最大相矛盾。所以不存在一点m能使得total(i, m) < 0. 即每一段total(i,m)都是大于等于零，即可以走完全程。