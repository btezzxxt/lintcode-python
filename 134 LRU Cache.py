# class LinkedListNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None

# class LRUCache:
#     """
#     @param: capacity: An integer
#     """
#     def __init__(self, capacity):
#         # do intialization if necessary
#         self.cap = capacity
#         self.num = 0
#         self.map = {}
#         self.DUMMY_HEAD = LinkedListNode(-1, None)
#         self.tail = self.DUMMY_HEAD

#     """
#     @param: key: An integer
#     @return: An integer
#     """
#     def get(self, key):
#         # write your code here
#         if key not in self.map:
#             return -1
#         else:
#             node = self.map[key].next
#             self.move_to_tail(node.key)
#             return node.value


#     """
#     @param: key: An integer
#     @param: value: An integer
#     @return: nothing
#     """
#     def set(self, key, value):
#         # write your code here
#         if key not in self.map:
#             node = LinkedListNode(key, value)
#             self.tail.next = node
#             self.map[key] = self.tail
#             self.tail = self.tail.next
#             self.num += 1
#             if self.num > self.cap:
#                 self.remove(self.DUMMY_HEAD.next.key)
#         else:
#             node = self.map[key].next
#             node.value = value
#             self.move_to_tail(key)

#     def remove(self, key):
#         pre_node = self.map[key]
#         if pre_node.next:
#             pre_node.next = pre_node.next.next
        
#         del self.map[key]

#         if pre_node.next:
#             self.map[pre_node.next.key] = pre_node
#         else:
#             self.tail = pre_node

#     def move_to_tail(self, key):
#         if self.tail.key == key:
#             return 
        
#         node = self.map[key].next
#         self.remove(key)

#         self.tail.next = node
#         self.map[node.key] = self.tail
#         self.tail = node

# a = LRUCache(2)
# print(a.set(2, 1))
# print(a.set(1, 1))
# print(a.get(2))
# print(a.set(4, 1))
# print(a.get(1))
# print(a.get(2))


class ListNodeA:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.size = capacity
        self.count = 0

        # cache key is key, value is pre node
        self.cache = {}
        self.dummy = ListNodeA(None, None)
        self.tail = self.dummy

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.cache:
            val = self.cache[key].next.val
            self.move_to_tail(key)
            return val
        else:
            return -1
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here

        # modify the value and move node to the end
        if key in self.cache:
            node = self.cache[key].next
            node.val = value
            self.move_to_tail(key)
        
        # create the node and add it to cache map
        else:
            # 1. remove the oldest from cache map / list first
            if self.count == self.size:
                del self.cache[self.dummy.next.key]
                self.dummy.next = self.dummy.next.next
                if self.dummy.next:
                    self.cache[self.dummy.next.key] = self.dummy
                self.count -= 1
            # 2. add the new one
            node = ListNodeA(key, value)
            self.tail.next = node
            self.cache[node.key] = self.tail
            self.tail = node
            self.count += 1

    def move_to_tail(self, key):
        pre = self.cache[key]
        node = pre.next
        if node.next:
            pre.next = node.next
            self.cache[node.next.key] = pre

            self.tail.next = node
            self.cache[node.key] = self.tail
            self.tail = node
            
a = LRUCache(1)
a.set(2, 1)
print(a.get(2))
a.set(3, 2)
print(a.get(2))
print(a.get(3))

