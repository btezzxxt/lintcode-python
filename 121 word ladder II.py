from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(end)
        dict.add(start)
        dis_map, shortest_dis = self.bfs(end, start, dict)
        print(dis_map)
        if shortest_dis == 0:
            return []
        res = []
        self.dfs(shortest_dis, start, end, [start], res, dis_map)
        return res 
    
    def dfs(self, dis, word, target, path, res, dis_map):
        if word == target:
            res.append(path[::])
            return 
        
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                newword = word[:i] + char + word[i + 1:]
                if newword in dis_map and dis_map[newword] == dis - 1:
                    path.append(newword)
                    self.dfs(dis - 1, newword, target, path, res, dis_map)
                    path.pop()

        
    
    def bfs(self, start, end, dict):
        dis_map = { start: 1 }
        
        queue = deque([start])
        level = 1
        while queue:
            level += 1 
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == end:
                    dis_map[end] = level - 1
                    return dis_map, level - 1 
                
                for i in range(len(cur)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newword = cur[: i] + char + cur[i + 1: ]
                        if newword in dict and newword not in dis_map:
                            dis_map[newword] = level
                            queue.append(newword)
        return dis_map, 0
        
from collections import deque
class Solution2:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        visited = set([start])
        
        queue = deque([start])
        level = 1
        while queue:
            level += 1 
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for i in range(len(cur)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newword = cur[:i] + char + cur[i + 1:]
                        if newword not in visited and newword in dict:
                            if newword == end:
                                return level
                            
                            visited.add(newword)
                            queue.append(newword)
        return 0

print(Solution2().ladderLength("a", "a", set(["b"])))