from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        indegree = [0] * (n + 1)
        first, second = None, None
        last = {}

        for u, v in edges:
            if indegree[v] == 1:
                first, second = last[v], [u, v]
            indegree[v] += 1
            last[v] = [u, v]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            if second and [u, v] == second:
                continue

            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return first if second else [u, v]
            parent[root_v] = root_u

        return second

sol = Solution()
print(sol.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))