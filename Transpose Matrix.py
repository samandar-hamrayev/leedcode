class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                new_matrix[i][j] = matrix[j][i]
        return new_matrix



sol = Solution()
print(sol.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
