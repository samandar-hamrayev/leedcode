class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)
        max_side = 0

        for i in range(m):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i][j - 1] == '1':
                    curr[j] = min(prev[j], curr[j - 1], prev[j - 1]) + 1
                    max_side = max(max_side, curr[j])
            prev = curr

        return max_side ** 2


sol = Solution()
print(sol.maximalSquare(matrix = [["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))

