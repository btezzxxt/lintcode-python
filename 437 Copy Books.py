import sys
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    # dp 超时了，大于O（nk）
    def copyBooks(self, pages, k):
        # write your code here
        n = len(pages)
        
        if k > n:
            k = n
            
        # a worker does all copy time
        sum = [0] * (n + 1)
        for i in range(1, n + 1):
            sum[i] = sum[i-1] + pages[i - 1]
        
        # init
        T = [[0] * (k + 1) for i in range(n + 1)]

        for i in range(1, k + 1):
            T[1][i] = sum[1]
        
        for i in range(1, n + 1):
            T[i][1] = sum[i]
        
        for j in range(2, k + 1):
            for i in range(2, n + 1):
                mini = sys.maxsize    
                for books_done_by_j_minus_1 in range(j - 1, i + 1):
                    # 比较2种情况， j-1个人copy了p本的时间，新加的人copy了i-p本的时间，较大者为cap花时间                  
                    temp = max(T[books_done_by_j_minus_1][j-1], T[i][1] - T[books_done_by_j_minus_1][1])  
                    # 比较每一种p的取法下， 找到时间最少的那个
                    mini = min(temp, mini)
                # 设为 i j
                T[i][j] = mini
        return T[n][k]                

    # binary search
"""
    def copyBooks(self, pages, k):
        # write your code here
        if len(pages) == 0 or k == 0:
            return 0
        
        l = 0 
        r = sys.maxsize
        while l + 1 < r:
            m = l + (r - l) // 2
            if self.canCopy(pages, m, k):
                r = m 
            else:
                l = m 
        if self.canCopy(pages, l, k):
            return l 
        return r

    def canCopy(self, pages, limit, k):
        nums = 1
        remain = limit
        for page in pages:
            if page > limit:
                return False
            
            if remain < page:      # 想办法把一个背包装到最满的贪心 因为顺序是固定的
                nums += 1
                remain = limit
            remain -= page
        return nums <= k        
"""
print(Solution().copyBooks([1,2], 5))
