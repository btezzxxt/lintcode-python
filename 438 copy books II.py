import sys
class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    # 二分
    def copyBooksII(self, n, times):
        l = 0
        r = sys.maxsize
        times.sort()
        while l + 1 < r:
            m = (l + r) // 2
            if self.canCopy(n, times, m):
                r = m
            else:
                l = m
        
        if self.canCopy(n, times, l):
            return l
        return r
    
    def canCopy(self, n, times, max_mins):
        remain = n
        for k in range(len(times)):
            remain -= max_mins // times[k]
            if remain <= 0:
                break
        if remain > 0:
            return False
        return True

    # # dp time out
    # def copyBooksIIdp(self, n, times):
    #     # write your code here
    #     k = len(times)
    #     times.sort()
    #     # dp[k][n] 前k个人完成了n本书所需要的最小时间
    #     dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(k + 1)]

    #     for j in range(1, n + 1):
    #         dp[1][j] = times[0] * j

    #     for i in range(2, k + 1):
    #         for j in range(1, n + 1):
    #             for l in range(j, i - 2, -1):
    #                 temp = max(dp[i - 1][l], (j - l) * times[i - 1])
    #                 dp[i][j] = min(dp[i][j], temp)
    #                 if (j - l) * times[i - 1] > dp[i - 1][l]:
    #                      break
        
    #     return dp[k][n]

    # @param n: an integer
    # @param times: a list of integers
    # @return: an integer
    # def copyBooksII(self, n, times):
    #     # write your code here
    #     k = len(times)
    #     ans = 0
    #     eachTime = []
    #     totalTime = []
    #     for i in range(k): self.heapAdd(eachTime, totalTime, times[i], 0)
    #     for i in range(n):
    #         ans = totalTime[0]
    #         x = eachTime[0]
    #         self.heapDelete(eachTime, totalTime)
    #         self.heapAdd(eachTime, totalTime, x, ans+x)
    #     ans = 0
    #     for i in range(len(totalTime)): ans = max(ans, totalTime[i])
    #     return ans

    # def heapAdd(self, eachTime, totalTime, et, tt):
    #     eachTime.append(et)
    #     totalTime.append(tt)
    #     n = len(eachTime)-1
    #     while n>0 and eachTime[n]+totalTime[n]<eachTime[(n-1)//2]+totalTime[(n-1)//2]:
    #         eachTime[n], eachTime[(n-1)//2] = eachTime[(n-1)//2], eachTime[n]
    #         totalTime[n], totalTime[(n-1)//2] = totalTime[(n-1)//2], totalTime[n]
    #         n = (n-1)//2

    # def heapDelete(self, eachTime, totalTime):
    #     n = len(eachTime)-1
    #     if n>=0: eachTime[0] = eachTime[n]
    #     if n>=0: totalTime[0] = totalTime[n]
    #     if len(eachTime)>0: eachTime.pop()
    #     if len(totalTime)>0: totalTime.pop()
    #     n = 0
    #     while n*2+1<len(eachTime):
    #         t = n*2+1
    #         if t+1<len(eachTime) and eachTime[t+1]+totalTime[t+1]<eachTime[t]+totalTime[t]: t += 1
    #         if eachTime[n]+totalTime[n]<=eachTime[t]+totalTime[t]: break
    #         eachTime[n], eachTime[t] = eachTime[t], eachTime[n]
    #         totalTime[n], totalTime[t] = totalTime[t], totalTime[n]
    #         n = t
            

# print(Solution().copyBooksII(5346, [243,882,424,995,703,9,361,61,522,377]))
print(Solution().copyBooksII(100, [1, 2]))