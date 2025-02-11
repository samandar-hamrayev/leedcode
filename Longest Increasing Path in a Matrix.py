class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]
        diractions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            max_path = 1
            for dx, dy in diractions:
                x, y = i + dx, j + dy
                if (
                        0 <= x < m
                        and 0 <= y < n
                        and matrix[x][y] > matrix[i][j]
                ):
                    max_path = max(max_path, 1 + dfs(x, y))
            memo[i][j] = max_path
            return max_path

        res = 0
        for i in range(m):
            for j_idx in range(n):
                res = max(res, dfs(i, j_idx))
        for row in memo:
            print(row)
        return res





