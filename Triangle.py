class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(
                    triangle[i+1][j],
                    triangle[i+1][j+1]
                )
        return triangle[0][0]



sol = Solution()
print(sol.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,7,8,3]]))