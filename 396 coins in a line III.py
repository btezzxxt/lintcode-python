class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        score_1p, score_2p = self.dfs(values, 0, len(values) - 1, {})
        return score_1p > score_2p

    # returns 1p scores, 2p scores
    def dfs(self, values, start, end, memo):
        if start == end:
            return values[start], 0
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        left_pick_2p_score, left_pick_1p_score = self.dfs(values, start + 1, end, memo)
        right_pick_2p_score, right_pick_1p_score = self.dfs(values, start, end - 1, memo)

        if left_pick_2p_score > right_pick_2p_score:
            score_2p =  right_pick_2p_score
            score_1p = right_pick_1p_score + values[end]
        else:
            score_2p = left_pick_2p_score
            score_1p = left_pick_1p_score + values[start]
        
        memo[(start, end)] = score_1p, score_2p

        return memo[(start, end)]

print(Solution().firstWillWin([1, 20, 4]))
