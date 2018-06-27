
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class UnionFind:
    def __init__(self):
        self.father = {}
    
    def add(self, x):
        if not x in self.father:
            self.father[x] = x

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
    
    def query(self):
        return self.father

class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes):
        # write your code here
        if len(nodes) == 0:
            return []
        
        ufind = UnionFind()
        for node in nodes:
            ufind.add(node.label)
            for neighbor in node.neighbors:
                ufind.add(neighbor.label)
                ufind.connect(node.label, neighbor.label)

        groups = {}
        for nodeValue in ufind.query().keys():
            root = ufind.find(nodeValue)
            if root in groups:
                groups[root].append(nodeValue) 
            else:
                groups[root] = [nodeValue]
        
        res = []
        for arr in groups.values():
            arr.sort()
            res.append(arr)
        return res


a = DirectedGraphNode(1)
b = DirectedGraphNode(2)
c = DirectedGraphNode(3)
d = DirectedGraphNode(4)
e = DirectedGraphNode(5)
f = DirectedGraphNode(6)

a.neighbors.append(b)
a.neighbors.append(d)
b.neighbors.append(d)
c.neighbors.append(e)
f.neighbors.append(e)



print(Solution().connectedSet2([a,b,c,d,e,f]))



        
