# from collections import deque
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.neighbors = []

# class Solution:
#     """
#     @param: numCourses: a total of n courses
#     @param: prerequisites: a list of prerequisite pairs
#     @return: the course order
#     """
#     def createGraph(self, numCourses, prerequisites):
#         g = {}
#         for i in range(numCourses):
#             g[i] = Node(i)
        
#         for pair in prerequisites:
#             g[pair[0]].neighbors.append(g[pair[1]])
#         return g
    
#     def getInDegreeMap(self, graph):
#         m = { node: 0 for node in graph.values() }
#         for node in graph.values():
#             for neighbor in node.neighbors:
#                 m[neighbor] = m[neighbor] + 1
#         return m

#     def findOrder(self, numCourses, prerequisites):
#         # write your code here
#         graph = self.createGraph(numCourses, prerequisites)
#         inDegreeMap = self.getInDegreeMap(graph)
#         order = []

#         queue = deque([])
#         for node in inDegreeMap.keys():
#             if inDegreeMap[node] == 0:
#                 queue.append(node)
        
#         while queue:
#             cur = queue.popleft()
#             order.append(cur.val)
#             for neighbor in cur.neighbors:
#                 inDegreeMap[neighbor] = inDegreeMap[neighbor] - 1
#                 if inDegreeMap[neighbor] == 0:
#                     queue.append(neighbor)
        
#         for value in inDegreeMap.values():
#             if value > 0:
#                 return []
#         return order

from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        self.indegree = 0

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        # build graph
        graph = {}
        for pre in prerequisites:
            c1 = pre[0]
            c2 = pre[1]
            if c1 not in graph:
                graph[c1] = Node(c1)
            if c2 not in graph:
                graph[c2] = Node(c2)
            graph[c2].neighbors.append(graph[c1])
            graph[c1].indegree += 1 
            
        # there are courses not showing in prerequisites relations, means no connection with other courses. thoses course have indegree 0 all the time
        for i in range(numCourses):
            if i not in graph:
                graph[i] = Node(i)
        
        # get starting nodes with indegree == 0
        nodes = []
        for node in graph.values():
            if node.indegree == 0:
                nodes.append(node)
        
        # topological sorting
        res = []
        queue = deque(nodes)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            for neighbor in node.neighbors:
                neighbor.indegree -= 1 
                if neighbor.indegree == 0:
                    queue.append(neighbor)
            del graph[node.val]
            
        if len(graph) == 0:
            return res 
        return []
        
                