import sys
class Solution:
    """
    @param dungeon: a 2D array
    @return: return a integer
    """
    def calculateMinimumHP(self, dungeon):
        # write your code here
        m = len(dungeon)
        n = len(dungeon[0])
        
        max_hp = [[-sys.maxsize for i in range(n + 1)] for i in range(m + 1)]
        min_cost = [[sys.maxsize for i in range(n + 1)] for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    max_hp[1][1] = dungeon[0][0]
                    if max_hp[1][1] < 0:
                        min_cost[1][1] = -max_hp[1][1] + 1
                    else:
                        min_cost[1][1] = 1
                else:
                    hp_from_top = max_hp[i - 1][j] + dungeon[i - 1][j - 1]
                    hp_from_left = max_hp[i][j - 1] + dungeon[i - 1][j - 1]
                    max_hp[i][j] = max(hp_from_top, hp_from_left)
                    
                    cost_from_top = max(-hp_from_top + 1, min_cost[i - 1][j])
                    cost_from_left = max(-hp_from_left + 1, min_cost[i][j - 1])
                    min_cost[i][j] = min(cost_from_top, cost_from_left)
        return min_cost[m][n]
                
                