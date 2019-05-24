
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

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

#         copied = {}

#         queue = deque([node])
#         head = UndirectedGraphNode(node.label)
#         copied[head.label] = head

#         while queue:
#             cur = queue.popleft()
#             curCopy = copied[cur.label]
           
#             for neighbor in cur.neighbors:
#                 # point to self, just add self to self neightbor, then continue
#                 if neighbor.label == curCopy.label:
#                     curCopy.neighbors.append(curCopy)
#                 else:
#                     # if neighbor is a new node, create and add the map
#                     if neighbor.label not in copied:
#                         copyN = UndirectedGraphNode(neighbor.label)
#                         copied[copyN.label] = copyN
#                         # add non-self new neighbor to queue waiting for process                        
#                         queue.append(neighbor)                        
#                     # if neighbor was created, get if from map
#                     else:
#                         copyN = copied[neighbor.label]

#                     # put in current copy's neighbor
#                     curCopy.neighbors.append(copyN)
#         return head

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
        org_clone = {node: UndirectedGraphNode(node.label)}
        
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in org_clone:
                    org_clone[nb] = UndirectedGraphNode(nb.label)
                    queue.append(nb)
        
        for node, clone in org_clone.items():
            for nb in node.neighbors:
                clone.neighbors.append(org_clone[nb])
        return org_clone[node]
        
z = UndirectedGraphNode(0)
one = UndirectedGraphNode(1)
two = UndirectedGraphNode(2)

z.neighbors.append(one)
z.neighbors.append(two)
one.neighbors.append(two)
two.neighbors.append(two)
Solution().cloneGraph(z)
