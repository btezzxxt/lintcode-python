# class GraphNode:
#     def __init__(self, val):
#         self.val = val
#         self.nbs = []
#         self.indegree = 0

# from heapq import heappush, heappop, heapify
# class Solution:
#     """
#     @param words: a list of words
#     @return: a string which is correct order
#     """
#     def alienOrder(self, words):
#         # Write your code here
#         nodes, edges = self.create_graph(words)
#         tp = self.get_topology(nodes, edges)
#         seq = "".join(tp)
#         return seq
        
#     def get_zero_indegree(self, nodes):
#         res = []
#         for node in nodes.values():
#             if node.indegree == 0:
#                 res.append(node.val)
#         return res
        
#     def sort(self, queue):
#         if queue and queue[0] > queue[-1]:
#             queue[0], queue[-1] = queue[-1], queue[0]
        
    
#     def get_topology(self, nodes, edges):
#         queue = self.get_zero_indegree(nodes)
#         heapify(queue)

#         tp = []
#         while queue:
#             cur = heappop(queue)
#             tp.append(cur)
#             cur_node = nodes[cur]
#             for nb in cur_node.nbs:
#                 nodes[nb].indegree -= 1 
#                 if nodes[nb].indegree == 0:
#                     heappush(queue, nb)

#         if len(tp) == len(nodes):
#             return tp 
#         else:
#             return []
            
        
#     def create_graph(self, words):
#         nodes = {}
#         edges = set()
        
#         for word in words:
#             for char in word:
#                 if char not in nodes:
#                     nodes[char] = GraphNode(char)
        
#         for i in range(len(words) - 1):
#             for j in range(min(len(words[i]), len(words[i + 1]))):
#                 char1 = words[i][j]
#                 char2 = words[i + 1][j]
#                 if char1 != char2:
#                     edges.add((char1, char2))
#                     break
        
#         for edge in edges:
#             # for a -> b
#             a = edge[0]
#             b = edge[1]
            
#             nodes[a].nbs.append(b)
#             nodes[b].indegree += 1         
#         return nodes, edges



class GraphNode:
    def __init__(self, val):
        self.val = val 
        self.neighbors = set()
        self.indegree = 0

from heapq import heappop, heappush
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        edges = self.get_edges(words)
        nodes = self.get_nodes(words)
        
        # add neighbors to nodes
        for edge in edges:
            node1 = nodes[edge[0]]
            node2 = nodes[edge[1]]
            if node2 not in node1.neighbors:
                node1.neighbors.add(node2)
                node2.indegree += 1 

        # get a topology
        heap = []
        for node in nodes.values():
            if node.indegree == 0:
                heappush(heap, (node.val, node))
        
        tpl = []        
        while heap:
            val, node = heappop(heap)
            tpl.append(val)
            for neighbor in node.neighbors:
                neighbor.indegree -= 1 
                if neighbor.indegree == 0:
                    heappush(heap, (neighbor.val, neighbor))
        
        print(tpl)
        if len(tpl) != len(nodes):
            return ""
        return "".join(tpl)
    
    def get_nodes(self, words):
        # val: node
        nodes = {}
        m = len(words)
        for i in range(m):
            n = len(words[i])
            for j in range(n):
                char = words[i][j]
                if char not in nodes:
                    nodes[char] = GraphNode(char)
        return nodes
        
        
                
    def get_edges(self, words):
        m = len(words)
        edges = []
        for i in range(1, m):
            str1 = words[i - 1]
            str2 = words[i]
            
            n = len(str1)
            n2 = len(str2)
            for j in range(n):
                if j < n2:
                    if str1[j] != str2[j]:
                        edges.append((str1[j], str2[j]))
                        break
                    else:
                        continue
        return edges
                