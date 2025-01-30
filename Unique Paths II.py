class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, n):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] if obstacleGrid[0][i] == 0 else 0

        for j in range(1, m):
            obstacleGrid[j][0] = obstacleGrid[j - 1][0] if obstacleGrid[j][0] == 0 else 0


        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]




sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,1]]))

