from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return  False
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col -1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        else:
            return False

sol = Solution()
print(sol.searchMatrix(
    matrix = [[1, 4],
            [2, 5]],
    target = 2))


