class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
        arr = [[] for _ in range(numRows)]
        index, direction = 0, 1
        for char in s:
            arr[index].append(char)
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction

        for i in range(numRows):
            arr[i] = ''.join(arr[i])

sol = Solution()
print(sol.convert("PAHNAPLSIIGYIR", 4))
