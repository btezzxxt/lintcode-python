from heapq import heappop, heappush
class Solution:
    """
    @param target: The target distance
    @param original: The original gas
    @param distance: The distance array
    @param apply: The apply array
    @return: Return the minimum times
    """
    def getTimes(self, target, original, distance, apply):
        # Write your code here
        heap = []
        cur_pos = -1
        cur_fuel = original
        count = 0
        
        n = len(distance)
        
        if cur_fuel >= target:
            return count
        
        while cur_pos <= n - 1:
            heap = []
            for i in range(cur_pos + 1, n):
                cost_to_reach = 0
                if cur_pos == -1:
                    cost_to_reach = distance[i]
                else:
                    cost_to_reach = distance[i] - distance[cur_pos]
                
                # can be reached
                if cost_to_reach <= cur_fuel:
                    heappush(heap, (-apply[i], i, cost_to_reach))
                else:
                    break
            
            # empty means no station can be reached
            if not heap:
                return -1
                    
            next_station = heappop(heap)
            next_fuel = -next_station[0]
            next_pos = next_station[1]
            cost_to_reach = next_station[2]
            
            count += 1
            cur_fuel = cur_fuel - cost_to_reach + next_fuel
            if cur_fuel >= target - distance[next_pos]:
                return count 
            cur_pos = next_pos
        
        return -1
        
        
        
        
        
        
        
        
        
        
        