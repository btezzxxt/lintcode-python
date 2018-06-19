UnionFindModule =  __import__("basic - unionfind")
uf = UnionFindModule.UnionFind([1,2,3])
print(uf.find(3))