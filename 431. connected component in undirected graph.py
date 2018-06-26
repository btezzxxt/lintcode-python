
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []




class UnionFind:
    def __init__(self):
        self.father = {}
        self.graphMap = {}
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connect(self, a, b):
        if not b in self.father:
            self.father[b] = b
            self.graphMap[b] = {b: True}
                    
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            
            for key, value in self.graphMap[root_a].items():
                if not key in self.graphMap[root_b]:
                    self.graphMap[root_b][key] = True
            
            del self.graphMap[root_a]
            
    def getGraph(self):
        return self.graphMap

    
    def addNode(self, node):
        if not node.label in self.father:
            self.father[node.label] = node.label
            self.graphMap[node.label] = {node.label: True}
        
        for neighbor in node.neighbors:
            self.connect(node.label, neighbor.label)

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):

        # write your code here
        uf = UnionFind()
        for node in nodes:
            uf.addNode(node)
            
        graph = uf.getGraph()
        res = []
        for valueMap in graph.values():
            arr = list(valueMap.keys())
            arr.sort()
       
            res.append(arr)
        
        return res

# {1,2,4#2,1,4#3,5#4,1,2#5,3}

a = UndirectedGraphNode(1)
b = UndirectedGraphNode(2)
c = UndirectedGraphNode(3)
d = UndirectedGraphNode(4)
e = UndirectedGraphNode(5)


a.neighbors.append(b)
a.neighbors.append(d)

b.neighbors.append(a)
b.neighbors.append(d)

c.neighbors.append(e)

d.neighbors.append(a)
d.neighbors.append(b)

e.neighbors.append(c)


        
print (Solution().connectedSet([a,b,c,d,e]))