class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1 

class HashHeap:
    def __init__(self):
        self.hash = {}
        self.heap = []
        self.count = 0
    
    def push(self, val):
        if val not in self.hash:
            node = Node(val)
            self.heap.append(node)
            idx = self._siftup(len(self.heap) - 1)
            self.hash[val] = idx
        else:
            idx = self.hash[val]
            self.heap[idx].count += 1
        self.count += 1

    def pop(self):
        node = self.heap[0]
        if node.count > 1:
            node.count -= 1
        else:
            self._switch(0, len(self.heap) - 1)
            self.heap.pop()
            del self.hash[node.val]
            self._siftdown(0)
        self.count -= 1
        return node.val
    
    def remove(self, val):
        idx = self.hash[val]
        node = self.heap[idx]
        if node.count > 1:
            node.count -= 1
        else:
            self._switch(idx, len(self.heap) - 1)
            self.heap.pop()
            del self.hash[val]
            if self._validIdx(idx):
                if self._validIdx(self._getParentId(idx)) and self.heap[self._getParentId(idx)].val > self.heap[idx].val:
                    self._siftup(idx)
                else:
                    self._siftdown(idx)
        self.count -= 1

    def top(self):
        return self.heap[0].val

    def isEmpty(self):
        return len(self.heap) == 0

    def _getParentId(self, idx):
        return (idx - 1) // 2
    
    def _getLeftChildId(self, idx):
        return idx * 2 + 1

    def _getRightChildId(self, idx):
        return idx * 2 + 2

    def _validIdx(self, idx):
        return 0 <= idx and idx < len(self.heap)
    
    def _switch(self, a, b):
        nodeA = self.heap[a]
        nodeB = self.heap[b]
        self.hash[nodeA.val] = b
        self.hash[nodeB.val] = a
        self.heap[b] = nodeA
        self.heap[a] = nodeB

    def _siftup(self, idx):
        while self._validIdx(idx):
            parentIdx = self._getParentId(idx)
            if self._validIdx(parentIdx) and self.heap[parentIdx].val > self.heap[idx].val:
                self._switch(idx, parentIdx)
                idx = parentIdx
            else:
                break
        return idx
    
    def _siftdown(self, idx):
        while self._validIdx(idx):
            leftIdx = self._getLeftChildId(idx)
            rightIdx = self._getRightChildId(idx)           
            if self._validIdx(leftIdx) and self._validIdx(rightIdx):
                if self.heap[leftIdx].val < self.heap[rightIdx].val and self.heap[leftIdx].val < self.heap[idx].val:
                    self._switch(leftIdx, idx)
                    idx = leftIdx
                elif self.heap[rightIdx].val < self.heap[leftIdx].val and self.heap[rightIdx].val < self.heap[idx].val:
                    self._switch(rightIdx, idx)
                    idx = rightIdx
                else:
                    break
            elif self._validIdx(leftIdx):
                if self.heap[leftIdx].val < self.heap[idx].val:
                    self._switch(leftIdx, idx)
                    idx = leftIdx                  
                else:
                    break
            elif self._validIdx(rightIdx):
                if self.heap[rightIdx].val < self.heap[idx].val:
                    self._switch(rightIdx, idx) 
                    idx = rightIdx               
                else:
                    break
            else:
                break
        return idx

class Event:
    def __init__(self, position, height, type):
        self.pos = position
        self.height = height
        self.type = type
    
    def __lt__(self, other):
        if self.pos == other.pos:
            if self.type == "1start" and other.type == "1start":
                return other.height < self.height 
            elif self.type == "2end" and other.type == "2end":
                return self.height < other.height 
            else:
                return self.type == "1start"
                
        return self.pos < other.pos 


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        events = []
        for building in buildings:
            events.append(Event(building[0], building[2], "1start"))
            events.append(Event(building[1], building[2], "2end"))
        events.sort()

        h_changes = []
        heap = HashHeap()

        for event in events:
            if event.type == "1start":
                max_height = -heap.top() if not heap.isEmpty() else 0
                if event.height > max_height:
                    h_changes.append([event.pos, event.height])
                heap.push(-event.height)
            else:
                heap.remove(-event.height)
                max_height = -heap.top() if not heap.isEmpty() else 0
                if event.height > max_height: 
                    h_changes.append([event.pos, max_height])
        
        res = []
        for i in range(0, len(h_changes) - 1):
            if h_changes[i][1] != 0:
                res.append([h_changes[i][0], h_changes[i + 1][0], h_changes[i][1]])
        return res

print(Solution().buildingOutline([[3,7,78],[4,5,313],[5,8,401],[6,10,242],[7,8,600],[8,12,466],[9,14,528],[10,13,370]]))