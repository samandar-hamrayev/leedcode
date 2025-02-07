from collections import deque


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]):
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len(set(find(i) for i in range(n)))

    def bfs(self, isConnected: list[list[int]]):
        n = len(isConnected)
        visited = [0] * n
        answer = 0
        for i in range(n):
            if visited[i] == 0:
                answer += 1
                visited[i] = 1
                queue = deque([i])
                while queue:
                    curr = queue.popleft()
                    for j in range(n):
                        if isConnected[curr][j] == 1 and visited[j] == 0:
                            queue.append(j)
                            visited[j] = 1
        return answer





sol = Solution()
print(sol.bfs(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))





