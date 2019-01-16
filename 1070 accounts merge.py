class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        uf = UnionFind()
        email_belong_to = {}
        for account in accounts:
            root = ''
            for i in range(1, len(account)):
                email = account[i]
                if email not in uf.father:
                    uf.add(email)                
                if i == 1:
                    root = uf.find(email)
                else:
                    uf.union(root, email)
            root = uf.find(root)
            email_belong_to[root] = account[0]
        
        emails_of_person = {}
        for account in accounts:
            emails = {}
            for i in range(1, len(account)):
                email = account[i]
                root = uf.find(email)
                if root not in emails_of_person:
                    emails_of_person[root] = set()
                emails_of_person[root].add(email)

        res = []
        for root, emails in emails_of_person.items():
            arr = []
            arr.append(email_belong_to[root])
            emails_to_append = sorted(list(emails))
        
            arr += emails_to_append
            res.append(arr)
        return res


class UnionFind:
    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
    
    def find(self, x):
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b