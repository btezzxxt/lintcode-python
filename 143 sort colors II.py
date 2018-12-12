class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        # 分治思想和快排的partition思想
        self.quickSort(colors, 0, len(colors) - 1, 1, k)

    def quickSort(self, colors, l, r, kL, kR):
        # 递归退出条件，或者l >= r 或者只有一种颜色
        if l < r and kL < kR:
            pivot = (kL + kR) // 2
            index = self.partition(colors, l, r, pivot) 

            # index是最后一个小于等于pivot的值
            # sort 左边到index（闭区间）中  kL 到pivot（闭区间）
            self.quickSort(colors, l, index, kL, pivot)
            # sort index + 1 到右边的范围，color的范围在pivot + 1 到kR
            self.quickSort(colors, index + 1, r, pivot + 1, kR)

    def partition(self, colors, l, r, pivot):       
        while l < r:
            # 右边要全部大于pivot
            while l < r and colors[r] > pivot:
                r = r - 1      
            # 左边要全部小于或者等于pivot
            while l < r and colors[l] <= pivot:
                l = l + 1
            
            # 找好了且左边不等于右边时互换
            if l < r:
                colors[l], colors[r] = colors[r], colors[l]

        # l是最好一个小于等于pivot的值
        return l



print(Solution().sortColors2([2,1,1,2,2], 2))
#1,1,2,3,4
