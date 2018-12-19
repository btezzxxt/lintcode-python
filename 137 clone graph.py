
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
