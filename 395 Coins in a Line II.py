class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if len(values) == 0:
            return False
        
        if len(values) < 3: 
            return True
        
        f = [0] * 3
        f[0] = values[-1]
        f[1] = values[-1] + values[-2]

        sum_ = values[-1] + values[-2]
       
        for i in range(2, len(values)):
            sum_ += values[-(i + 1)]
            f[i % 3] = sum_ - min(f[(i - 1) % 3], f[(i - 2) % 3])
        
        return f[i % 3] > f[(i - 1) % 3] or f[i % 3] > f[(i - 2) % 3]

print(Solution().firstWillWin([1,2,2]))