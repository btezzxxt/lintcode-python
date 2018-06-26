
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class UnionFind:
    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b):
        if not b in self.father:
            return
        root_a = self.find(a)        
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1
    
    def add(self, x):
        if not x in self.father:
            self.father[x] = x
            self.count += 1

    def query(self):
        return self.count
        


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def getId(self, x, y, m):
        return x*m + y

    def numIslands2(self, n, m, operators):
        # write your code here
        for i in range(len(operators)):
            operators[i] = Point(operators[i][0], operators[i][1])

        if m <= 0 or n <= 0 or len(operators) <= 0:
            return []

        bigger = m if m > n else n

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0 ,1]
        
        res = [0] * len(operators)
        unionFind = UnionFind()

        for i, point in enumerate(operators):
            pid = self.getId(point.x, point.y, bigger)
            if i == 26:
                print (point.x, point.y)
            unionFind.add(pid)
            for j in range(4):
                new_x = point.x + dx[j]
                new_y = point.y + dy[j]
                if new_x >= 0 and new_x < n and new_y >= 0 and new_y <= m:
                    unionFind.union(pid, self.getId(new_x, new_y, bigger))
                res[i] = unionFind.query()
        return res

print(Solution().numIslands2(8,14,
[[0,9],[5,4],[0,12],[6,9],
[6,5],[0,4],[4,11],[0,0],[3,5],[6,7],
[3,12],[0,5],[6,13],[7,5],[3,6],[4,4],[0,8],[3,1],[4,6],[6,1],[5,12],[3,8],[7,0],[2,9],
[1,4],[3,0],[1,13],[2,13],[6,0],[6,4],[0,13],[0,3],[7,4],[1,8],[5,5],[5,7],[5,10],[5,3],[6,10],[6,2],[3,10],[2,7],[1,12],[5,0],[4,5],[7,13],[3,2]]))