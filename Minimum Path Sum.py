class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        for j in range(1, m):
            grid[j][0] += grid[j-1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


sol = Solution()
print(sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
