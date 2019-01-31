class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        prefix_sum = [0 for _ in range(n + 1)]
        for i in range(n):
            index = i + 1
            prefix_sum[index] = prefix_sum[index - 1] + A[i]

        count = 0

        l_let_sum_smaller_eq_end, r_let_sum_greater_eq_start = 0, 0
        for i in range(1, n + 1):
            # i, end point

            # > end because we'd like to find the fist qualified that prefix i - prefix l that sum <= end
            while l_let_sum_smaller_eq_end < i and prefix_sum[i] - prefix_sum[l_let_sum_smaller_eq_end] > end:
                l_let_sum_smaller_eq_end += 1
            # >= start because we'd like to find the first unqualified position that sum < start
            while r_let_sum_greater_eq_start < i and prefix_sum[i] - prefix_sum[r_let_sum_greater_eq_start] >= start:
                r_let_sum_greater_eq_start += 1
            
            # from [l, l + 1, ..., r - 1] there are r - l nums e.g. in [2,3,4] l = 2, r = 5, there are 5-2 =3 numbers
            count += r_let_sum_greater_eq_start - l_let_sum_smaller_eq_end
        
        return count

print(Solution().subarraySumII([1,2,3,4], 1,3))