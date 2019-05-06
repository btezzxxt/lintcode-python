class UnionFind:
    def __init__(self):
        self.father = {} 
        self.count = 0
        
    def add(self, x):
        if x not in self.father:
            self.father[x] = x 
            self.count += 1 
    
    def find(self, x):
        if self.father[x] == x:
            return x 
        
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b 
            self.count -= 1 


class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        uf = UnionFind()
        
        for set in sets:
            for i in range(len(set)):
                uf.add(set[i])
                if i + 1 < len(set):
                    uf.add(set[i + 1])
                    uf.union(set[i], set[i + 1])
        
        return uf.count 
                
        