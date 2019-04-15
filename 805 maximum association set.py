class UnionFind:
    def __init__(self):
        self.father = {}
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = x 
        
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
    
    def update(self):
        for x in self.father.keys():
            self.find(x)
    
    def get_children_list(self):
        res = {}
        for kid, father in self.father.items():
            if father not in res:
                res[father] = []
            res[father].append(kid)
        return list(res.values())
            
            

class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        n = len(ListA)
        
        uf = UnionFind()
        for i in range(n):
            uf.add(ListA[i])
            uf.add(ListB[i])
            uf.union(ListA[i], ListB[i])
        
        uf.update()
        as_sets = uf.get_children_list()
        as_sets.sort(key=lambda x: -len(x))
        return as_sets[0]
        
        