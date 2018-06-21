class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        self.count = {}
        for i in range(n):
            self.father[i + 1] = i + 1
            self.count[i + 1] = 1

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)    
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count[root_b] += self.count[root_a]
            del self.count[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.count[self.find(a)]


a = ConnectingGraph2(5)
print(a.query(1))
print(a.connect(1, 2))
print(a.query(1))
print(a.connect(2, 4))
print(a.query(1))
print(a.connect(1, 4))
print(a.query(1))