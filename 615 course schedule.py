from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        graph = {}
        for i in range(numCourses):
            graph[i] = Node(i)
        
        for pair in prerequisites:
            graph[pair[0]].neighbors.append(graph[pair[1]])
        # graph construction complete

        inDegreeMap = self.getAllInDegree(graph)
        queue = deque([])

        for node in inDegreeMap.keys():
            if inDegreeMap[node] == 0:
                queue.append(node)

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                inDegreeMap[neighbor] = inDegreeMap[neighbor] - 1
           
                if inDegreeMap[neighbor] == 0:
                    queue.append(neighbor)

        for inDegree in inDegreeMap.values():
            if inDegree > 0:
                return False
        return True

    def getAllInDegree(self, graph):
        nodes = graph.values()
        map_ = { node: 0 for node in nodes }

        for node in nodes:
            for neighbor in node.neighbors:
                map_[neighbor] = map_[neighbor] + 1
        return map_
print(Solution().canFinish(2, [[1,0]]))
