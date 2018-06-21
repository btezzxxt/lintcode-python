class UnionFind:
    def __init__(self, arr):
        self.__father = {}
        for i in arr:
            self.__father[i] = i

    def find(self, x):
        if self.__father[x] == x:
            return x
        self.__father[x] = self.find(self.__father[x]) 
        return self.__father[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.__father[root_a] = root_b

uf = UnionFind([1,2,3,4,5,6])
uf.union(1,6)

print(1, ' - ', uf.find(1), '\n')
print(6, ' - ', uf.find(6), '\n')


