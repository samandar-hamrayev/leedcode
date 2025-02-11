from collections import defaultdict, deque


class Solution:
    def minMaxWeight(self, n: int, edges: list[list[int]], threshold: int) -> int:
        left, right = 1, max(w for _, _, w in edges)
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if self.is_valid(n, edges, threshold, mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

    def is_valid(self, n, edges, threshold, max_weight):
        graph = defaultdict(list)
        out_degree = defaultdict(int)

        for u, v, w in edges:
            if w <= max_weight:
                graph[u].append((v, w))
                out_degree[u] += 1

        for node in range(n):
            if out_degree[node] > threshold:
                return False

        q = deque([0])
        visited = set()
        while q:
            node = q.popleft()
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)

        return len(visited) == n


sol = Solution()
print(sol.minMaxWeight(n=5, edges=[[1, 0, 1], [2, 0, 2], [3, 0, 1], [4, 3, 1], [2, 1, 1]], threshold=2))