import sys
from collections import deque
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        # bfs 每次去掉一个位置的valid word
        # 加一个 visited
        # find - found的用法还是第一次

        queue = deque([s])
        min_len = len(s)
        visited = set([s])
        
        while queue:
            cur = queue.popleft()
            for word in dict:
                found = cur.find(word)
                while found != -1:
                    string = cur[: found] + cur[found + len(word):]
                    if len(string) < min_len:
                        min_len = len(string)
                    if string not in visited:    
                        queue.append(string)
                        visited.add(string)
                    found = cur.find(word, found + len(word) + 1)
        return min_len
            
        