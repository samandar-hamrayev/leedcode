class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parents = [i for i in range(1, n+1)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            parents[ry] = rx
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
sol = Solution()
print(sol.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))

