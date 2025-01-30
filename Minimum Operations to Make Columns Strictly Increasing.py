class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        total = 0

        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] <= grid[i-1][j]:
                    total += grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] = grid[i-1][j] + 1

        return total


sol = Solution()
print(sol.minimumOperations(grid = [[3,2],[1,3],[3,4],[0,1]]))
