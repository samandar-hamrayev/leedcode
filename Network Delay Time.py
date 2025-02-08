import heapq
from collections import defaultdict, deque


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Bu yechimda biz heap ishlatib muammoni hal qilamiz
        :param times:
        :param n:
        :param k:
        :return:
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        dist = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (time + weight, neighbor))
        return max(dist.values()) if len(dist) == n else - 1

    def networkDelayTime_bfs(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Bu yechimda heap ishlatmasdan muammoni hal qilamiz
        :param times:
        :param n:
        :param k:
        :return:
        """
        graph = defaultdict(list)
        for sender, receiver, cost in times:
            graph[sender].append((receiver, cost))
        distance = {k:0}
        queue = deque([(0, k)])
        while queue:
            time, node = queue.popleft()
            for neighbor, weight in graph[node]:
                new_time = time + weight
                if neighbor not in distance or distance[neighbor] > new_time:
                    distance[neighbor] = new_time
                    queue.append((new_time, neighbor))

        return max(distance.values()) if len(distance) == n else - 1




sol = Solution()
print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(sol.networkDelayTime_bfs(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
