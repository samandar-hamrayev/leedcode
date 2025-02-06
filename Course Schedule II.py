from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prev in prerequisites:
            graph[prev].append(course)
            in_degree[course] += 1

        queue = deque([degree for  degree in range(numCourses) if in_degree[degree] == 0])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []



sol  = Solution()
print(sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))