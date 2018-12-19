from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def createGraph(self, numCourses, prerequisites):
        g = {}
        for i in range(numCourses):
            g[i] = Node(i)
        
        for pair in prerequisites:
            g[pair[0]].neighbors.append(g[pair[1]])
        return g
    
    def getInDegreeMap(self, graph):
        m = { node: 0 for node in graph.values() }
        for node in graph.values():
            for neighbor in node.neighbors:
                m[neighbor] = m[neighbor] + 1
        return m

    def findOrder(self, numCourses, prerequisites):
        # write your code here
        graph = self.createGraph(numCourses, prerequisites)
        inDegreeMap = self.getInDegreeMap(graph)
        order = []

        queue = deque([])
        for node in inDegreeMap.keys():
            if inDegreeMap[node] == 0:
                queue.append(node)
        
        while queue:
            cur = queue.popleft()
            order.append(cur.val)
            for neighbor in cur.neighbors:
                inDegreeMap[neighbor] = inDegreeMap[neighbor] - 1
                if inDegreeMap[neighbor] == 0:
                    queue.append(neighbor)
        
        for value in inDegreeMap.values():
            if value > 0:
                return []
        return order