class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        for i in range(n):
            self.father[i+1] = i+1
        self.count = n
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
            self.count -= 1
        
    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.count