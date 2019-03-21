# class Connection:

#     def __init__(self, city1, city2, cost):
#         self.city1, self.city2, self.cost = city1, city2, cost

#     # def __lt__(self, b):
#     #     if self.cost != b.cost:
#     #         return self.cost < b.cost
        
#     #     if self.city1 != b.city1:
#     #         return self.city1 < b.city1
        
#     #     if self.city2 != b.city2:
#     #         return self.city1 < b.city2

#     # def __repr__(self):
#     #     return str([self.city1, self.city2, self.cost])

# def comp(a, b):
#     if a.cost != b.cost:
#         return a.cost - b.cost
    
#     if a.city1 != b.city1:
#         if a.city1 < b.city1:
#             return -1
#         else:
#             return 1

#     if a.city2 == b.city2:
#         return 0
#     elif a.city2 < b.city2:
#         return -1
#     else:
#         return 1

# import functools
# class Solution:
#     # @param {Connection[]} connections given a list of connections include two cities and cost
#     # @return {Connection[]} a list of connections from results
#     def lowestCost(self, connections):
#         # Write your code here
#         connections.sort(key=functools.cmp_to_key(comp))
#         father = {}
#         for connection in connections:
#             if connection.city1 not in father:
#                 father[connection.city1] = connection.city1
            
#             if connection.city2 not in father:
#                 father[connection.city2] = connection.city2

#         results = []
#         for connection in connections:
#             root1 = self.find(connection.city1, father)
#             root2 = self.find(connection.city2, father)
#             if root1 != root2:
#                 father[root1] = root2
#                 results.append(connection)

#         if len(results)!= len(father) - 1:
#             return []
#         return results
    
#     def find(self, city, father):
#         if father[city] == city:
#             return city
#         father[city] = self.find(father[city], father)
#         return father[city]

# a = [Connection("Acity","Bcity",1),Connection("Acity","Ccity",2),Connection("Bcity","Ccity",3)]
# print(Solution().lowestCost(a))

class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        return False

class UnionFind:
    def __init__(self):
        self.father = {}
    
    def add(self, item):
        if item not in self.father:
            self.father[item] = item
    
    def find(self, item):
        if self.father[item] == item:
            return item
        self.father[item] = self.find(self.father[item])
        return self.father[item]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        connections.sort()
        handler = UnionFind()
        res = []

        hashset = set() # city numbers
        for connection in connections:
            hashset.add(connection.city1)
            hashset.add(connection.city2)

        for connection in connections:
            city1 = connection.city1
            city2 = connection.city2
            handler.add(city1)
            handler.add(city2)
            if handler.find(city1) != handler.find(city2):
                res.append(connection)
                handler.union(city1, city2)
            if len(res) == len(hashset) - 1:
                return res
        return []
            
