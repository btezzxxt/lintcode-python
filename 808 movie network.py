class Node:
    def __init__(self, id, rating):
        self.id = id 
        self.rating = rating
        self.nb = set()

from heapq import heappop, heappush
from collections import deque
class Solution:
    """
    @param rating: the rating of the movies
    @param G: the realtionship of movies
    @param S: the begin movie
    @param K: top K rating 
    @return: the top k largest rating moive which contact with S
    """
    def topKMovie(self, rating, G, S, K):
        # Write your code here
        nodes = {}
        n = len(rating)
        for i in range(n):
            node = Node(i, rating[i])
            nodes[node.id] = node 
        
        for edge in G:
            for i in range(1, len(edge)):
                id1 = edge[i - 1]
                id2 = edge[i]
                nodes[id1].nb.add(id2)
                nodes[id2].nb.add(id1)
            
        start = nodes[S]
        heap = []
        
        queue = deque([start])
        visited = set([S])
        while queue:
            cur = queue.popleft()
            if cur.id not in visited:
                heappush(heap, (-cur.rating, cur.id))
                visited.add(cur.id)
            for neighbor in cur.nb:
                if neighbor not in visited:
                    queue.append(nodes[neighbor])
        
        res = []
        while heap and K > 0:
            res.append(heappop(heap)[1])
            K -= 1
            
        return res 
                    