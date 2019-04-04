"""
题目：
写一个compare 方法， 比较两个字符串的大小。字符串可以包含任何的ASCII字符。要求，把字符串中的数字当成一个整体比较， 比如：

s1： abc0123ac
s2:   abc5ac
返回 1， s1 > s2. 因为 0123 > 5.

s1:  abc555
s2:  abcd
返回 1，s1 > s2. 这时候需要比较555和d的ASCII number的大小。

s1:  abc0123. From 1point 3acres bbs
s2:  abc123
返回 0， s1 = s2. 因为0123 = 123

s1:  abc097
s2:  abca
返回 0， s1 = s2. 因为 a的ASCII number = 97

s1: abc
s2: abcd
返回 -1， s1 < s2. 字典顺序

int compare(String s1, String s2) ;
"""

"""
给一个矩阵
类似这样的
[[0, 0, 1, 1, 1],
[0, 1, 1, 1, 1],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 1]]
1. 每一个cell 要不是0 要不是1
2. 每一行只要发现一个1， 剩下的都是1
3. 这个数组是正方形的
问题：找到最左边的有1的列
   
    这个例子的结果是 2


我的方法：对每一个row 用binary search . 1point3acres
"""


"""
有一个数组 例如[1,2,3,4,5]没有重复的数字，从中随机选出包含k个字母的组合，要求所有数字被选中的概率相等
follow up:不用额外的list，优化时间空间复杂度，到最后讲了思路，没时间写代码，两天之后通知fail
"""

"""
https://www.geeksforgeeks.org/find-local-minima-array/
"""