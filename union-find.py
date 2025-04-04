class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x # kattaroq daraxtga bog'lanyapti
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1



uf = UnionFind(10)
uf.union(0, 1)
uf.union(1, 2)
uf.union(2, 3)
uf.union(3, 4)

print(uf.find(3))


