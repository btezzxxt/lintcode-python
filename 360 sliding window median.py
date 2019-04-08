class Node:
    def __init__(self, val):
        self.val = val 
        self.count = 1

class Hashheap:
    def __init__(self):
        self.hash = {}
        self.heap = []
        self.total = 0
    
    def push(self, val):
        if val in self.hash:
            i = self.hash[val]
            self.heap[i].count += 1 
        else:
            node = Node(val)
            self.heap.append(node)
            index = len(self.heap) - 1
            self.hash[val] = index
            self._siftup(index)
        self.total += 1

    def pop(self):
        node = self.heap[0]
        if node.count > 1:
            node.count -= 1
        else:
            last_index = len(self.heap) - 1
            self._swap(0, last_index)
            self.heap.pop()
            del self.hash[node.val]
            self._siftdown(0)
        self.total -= 1
        return node.val

    def top(self):
        return self.heap[0].val

    def remove(self, val):
        i = self.hash[val]
        node = self.heap[i]
        if node.count > 1:
            node.count -= 1
        else:
            last_index = len(self.heap) - 1
            self._swap(i, last_index)
            self.heap.pop()
            del self.hash[val]

            if i != last_index:
                self._siftup(i)
                self._siftdown(i)
        self.total -= 1
        
    def _siftup(self, index):
        parent_i = (index - 1) // 2
        while self._valid_index(parent_i):
            if self.heap[parent_i].val > self.heap[index].val:
                self._swap(parent_i, index)
                index = parent_i
                parent_i = (index - 1) // 2
            else:
                break

    def _siftdown(self, index):
        l = index * 2 + 1
        r = index * 2 + 2
        if self._valid_index(l) and self._valid_index(r):
            if self.heap[index].val > self.heap[l].val and self.heap[l].val < self.heap[r].val:
                self._swap(index, l)
                self._siftdown(l)
            elif self.heap[index].val > self.heap[r].val and self.heap[r].val < self.heap[l].val:
                self._swap(index, r)
                self._siftdown(r)
        elif self._valid_index(l):
            if self.heap[index].val > self.heap[l].val:
                self._swap(index, l)
                self._siftdown(l)
        elif self._valid_index(r):
            if self.heap[index].val > self.heap[r].val:
                self._swap(index, r)
                self._siftdown(r)

    def _swap(self, i, j):
        a = self.heap[i]
        b = self.heap[j]
        self.heap[i], self.heap[j] = b, a 
        self.hash[a.val] = j 
        self.hash[b.val] = i

    def _valid_index(self, index):
        if index >= 0 and index < len(self.heap):
            return True 
        return False

    def count(self):
        return self.total

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums:
            return []
        
        if k == 0:
            return []
        
        res = []
        min_heap = Hashheap()
        max_heap = Hashheap()
        n = len(nums)       
        if k >= n:
            for i in range(n):
                self.add_to_heap(nums[i], min_heap, max_heap)
            res.append(-max_heap.top())
        else:
            for i in range(k):
                self.add_to_heap(nums[i], min_heap, max_heap)
            res.append(-max_heap.top())

            for i in range(k, n):
                self.add_to_heap(nums[i], min_heap, max_heap)
                self.remove_from_heap(nums[i - k], min_heap, max_heap)
                res.append(-max_heap.top())
        return res
    
    def add_to_heap(self, num, min_heap, max_heap):
        if max_heap.count() == 0:
            max_heap.push(-num)
        else:
            median = -max_heap.top()
            if num <= median:
                max_heap.push(-num)
            else:
                min_heap.push(num)
            self.balance(min_heap, max_heap)
    
    def remove_from_heap(self, num, min_heap, max_heap):
        median = - max_heap.top()
        if num > median:
            min_heap.remove(num)
        else:
            max_heap.remove(-num)
        self.balance(min_heap, max_heap)

    def balance(self, min_heap, max_heap):
        if max_heap.count() == min_heap.count():
            return 
        elif max_heap.count() - min_heap.count() == 1:
            return 
        elif max_heap.count() < min_heap.count():
            val = min_heap.pop()
            max_heap.push(-val)
        else:
            val = -max_heap.pop()
            min_heap.push(val)
        
