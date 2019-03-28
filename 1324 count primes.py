class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        if n <= 1:
            return 0
        
        prime_checker = [True] * n
        count = 0
        for i in range(2, n):
            if prime_checker[i]:
                count += 1
                for j in range(2, n):
                    if i * j >= n:
                        break
                    prime_checker[i * j] = False
        return count 
        
# test case 5 -> 2
# test case 20 -> 8
                    