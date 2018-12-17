from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dic = set(dict)
        dic.add(end)
        count = 0
        queue = deque([start])
        visited = set([start])

        while queue:
            count += 1
            for _ in range(len(queue)):           
                cur = queue.popleft()
                if cur == end:
                    return count
                for i in range(len(cur)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if cur[i] != char:
                            newword = cur[0:i] + char + cur[i+1:]
                            if newword in dic and newword not in visited:
                                queue.append(newword)
                                visited.add(newword)
        return 0 

        
print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))