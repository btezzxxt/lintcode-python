class UnionFind:
    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i 

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    def canConnect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        return False if root_a == root_b else True
        
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if n > 1 and len(edges) == 0:
            return False
            
        if n == 1 and len(edges) == 0:
            return True
            
        if n > len(edges) + 1:
            return False

        uf = UnionFind(n)
        for pair in edges:
            if uf.canConnect(pair[0], pair[1]):
                uf.connect(pair[0], pair[1])
            else:
                return False
        return True

