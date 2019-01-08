class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        count = m + n - 1
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[count] = A[m - 1]
                m -= 1
            else:
                A[count] = B[n - 1]
                n -= 1
            count -= 1
        
        while m > 0:
            A[count] = A[m - 1]
            count -= 1
            m -= 1
        
        while n > 0:
            A[count] = B[n - 1]
            count -= 1
            n -= 1
        
        return A
        