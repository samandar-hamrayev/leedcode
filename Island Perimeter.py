class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])

        count = 0
        for j in range(row):
            for i in range(col):
                if grid[j][i] == 1:
                    count += 4
                    if j > 0 and grid[j-1][i] == 1:
                        count -= 2

                    if i > 0 and grid[j][i-1] == 1:
                        count -= 2
        return count


sol = Solution()
print(sol.islandPerimeter(grid = [[1]]))
