
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node

        copied = {}

        queue = deque([node])
        head = UndirectedGraphNode(node.label)
        copied[head.label] = head

        while queue:
            cur = queue.popleft()
            curCopy = copied[cur.label]
           
            for neighbor in cur.neighbors:
                # point to self, just add self to self neightbor, then continue
                if neighbor.label == curCopy.label:
                    curCopy.neighbors.append(curCopy)
                else:
                    # if neighbor is a new node, create and add the map
                    if neighbor.label not in copied:
                        copyN = UndirectedGraphNode(neighbor.label)
                        copied[copyN.label] = copyN
                        # add non-self new neighbor to queue waiting for process                        
                        queue.append(neighbor)                        
                    # if neighbor was created, get if from map
                    else:
                        copyN = copied[neighbor.label]

                    # put in current copy's neighbor
                    curCopy.neighbors.append(copyN)
        return head

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# from collections import deque
# class Solution:
#     """
#     @param: node: A undirected graph node
#     @return: A undirected graph node
#     """
#     def cloneGraph(self, node):
#         # write your code here
#         if not node:
#             return node
        
#         # old graph nodes status
#         added = set()
#         queue = deque([node])
#         added.add(node.label)        
        
#         # new graph nodes status
#         created = {}
#         head = UndirectedGraphNode(node.label)
#         created[head.label] = head
        

        
#         while queue:
#             old_cur = queue.popleft()
#             new_cur = created[old_cur.label]
            
#             # adding neighbor for the cloned node
#             for neighbor in old_cur.neighbors:
#                 if neighbor.label not in created:
#                     new_neighbor = UndirectedGraphNode(neighbor.label)
#                     created[new_neighbor.label] = new_neighbor
#                     new_cur.neighbors.append(new_neighbor)
#                 else:
#                     new_cur.neighbors.append(created[neighbor.label])
                
#                 # 如果这个neighbor还没有被添加过，放入queue并记录  
#                 if neighbor.label not in added:
#                     queue.append(neighbor)
#                     added.add(neighbor.label)
#         return head

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None

        nodes = self.bfs(node)
        
        mapping = {}
        for node_org in nodes:
            mapping[node_org] = UndirectedGraphNode(node_org.label) 
        
        for node_org in nodes:
            node_copy = mapping[node_org]
            for nb in node_org.neighbors:
                nb_copy = mapping[nb]
                node_copy.neighbors.append(nb_copy)
        return mapping[node]
    
    def bfs(self, node):
        queue = deque([node])
        visited = set([node])
        
        nodes = [] 
        while queue:
            cur = queue.popleft()
            nodes.append(cur)
            for nb in cur.neighbors:
                if nb not in visited:
                    queue.append(nb)
                    visited.add(nb)
        return nodes
        
        
        
one = UndirectedGraphNode(1)
two = UndirectedGraphNode(2)
one.neighbors.append(two)
two.neighbors.append(one)
Solution().cloneGraph(one)
