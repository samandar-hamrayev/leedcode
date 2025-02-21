class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(board), len(board[0])

        def dfs(y, x):
            board[y][x] = "#"
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < row and 0 <= nx < col and board[ny][nx] == 'O':
                    dfs(ny, nx)

        for i in range(col):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[row - 1][i] == 'O':
                dfs(row - 1, i)

        for j in range(row):
            if board[j][0] == 'O':
                dfs(j, 0)
            if board[j][col - 1] == 'O':
                dfs(j, col - 1)

        for j in range(row):
            for i in range(col):
                if board[j][i] == "O":
                    board[j][i] = "X"
                elif board[j][i] == "#":
                    board[j][i] = "O"





board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

sol = Solution()
print(sol.solve(board))
for row in board:
    print(row)




