class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1 

class HashHeap:
    def __init__(self):
        self.hash = {}
        self.heap = []
    
    def push(self, val):
        if val not in self.hash:
            node = Node(val)
            self.heap.append(node)
            idx = self._siftup(len(self.heap) - 1)
            self.hash[val] = idx
        else:
            idx = self.hash[val]
            self.heap[idx].count += 1

    def pop(self):
        node = self.heap[0]
        if node.count > 1:
            node.count -= 1
        else:
            self._switch(0, len(self.heap) - 1)
            self.heap.pop()
            del self.hash[node.val]
            self._siftdown(0)
    
    def delete(self, val):
        idx = self.hash[val]
        node = self.heap[idx]
        if node.count > 1:
            node.count -= 1
        else:
            self._switch(idx, len(self.heap) - 1)
            self.heap.pop()
            del self.hash[val]
            if self._validIdx(self._getParentId(idx)) and self.heap[self._getParentId(idx)].val > self.heap[idx].val:
                self._siftup(idx)
            else:
                self._siftdown(idx)

    def peek(self):
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
    
    def __repr__(self):
        s = []
        for node in self.heap:
            for i in range(node.count):
                s.append(node.val)
        return str(s)

# hh = HashHeap()
# hh.push(2)
# hh.push(2)
# hh.push(2)
# hh.push(7)
# hh.push(15)
# hh.push(13)
# hh.push(8)
# hh.push(1)
# hh.push(20)
# hh.push(25)

# print(hh)
# hh.peek()
# hh.pop()
# print(hh)
# hh.peek()

# hh.delete(2)
# print(hh)
# hh.delete(7)
# print(hh)

    
    






    