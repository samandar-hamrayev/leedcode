class Solution:
    def getRow1th(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]

        current_row = [1] * (rowIndex + 1)
        prev_row = self.getRow1th(rowIndex - 1)
        for i in range(1, len(current_row) - 1):
            current_row[i] = prev_row[i] + prev_row[i - 1]

        return current_row


    def getRow2th(self, rowindex: int) -> list[int]:
        current_row = [1] * (rowindex + 1)

        for i in range(2, rowindex + 1):
            for j in range(i-1, 0, -1):
                current_row[j] = current_row[j] + current_row[j-1]

        return current_row

sol = Solution()
print(sol.getRow2th(4))

