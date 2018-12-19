class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        order = []
        
        indegree = { node: 0 for node in graph }
    
        for node in graph:
            for nei in node.neighbors:
                indegree[nei] += 1
        
        zeroIndegrees = [node for node in indegree.keys() if indegree[node] == 0]
        queue = deque(zeroIndegrees)
        
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for nei in cur.neighbors:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return order