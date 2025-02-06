from collections import defaultdict, deque


class Solution:
    def canFinish_dfs(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)

        for course, precourse in prerequisites:
            graph[precourse].append(course)

        visited = set()
        onpath = set()

        def dfs(node):
            if node in onpath:
                return False

            if node in visited:
                return True

            onpath.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            onpath.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return  False
        return True

    def canFinish_bfs(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, precourse in prerequisites:
            graph[precourse].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            count += 1
            curr = queue.popleft()
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses


sol = Solution()
print(sol.canFinish_bfs(numCourses = 2, prerequisites = [[1,0]]))
