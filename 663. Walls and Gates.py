from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms or not rooms[0]:
            return
        m = len(rooms)
        n = len(rooms[0])
        inf = pow(2, 31) - 1 

        visited = set()
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        level = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if rooms[i][j] == inf:
                    rooms[i][j] = level

                for k in range(4):
                    di = i + dx[k]
                    dj = j + dy[k]
                    if di >=0 and di < m and dj >= 0 and dj < n and rooms[di][dj] == inf and (di, dj) not in visited:
                        queue.append((di, dj))
                        visited.add((di, dj))
            level += 1
        