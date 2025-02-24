class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(row, col, ch):
            block_row, block_col = row // 3, col // 3
            return not (ch in rows[row] or ch in cols[col] or ch in blocks[block_row][block_col])

        def place_number(row, col, ch):
            board[row][col] = ch
            rows[row].add(ch)
            cols[col].add(ch)
            blocks[row // 3][col // 3].add(ch)

        def remove_number(row, col, ch):
            board[row][col] = "."
            rows[row].remove(ch)
            cols[col].remove(ch)
            blocks[row // 3][col // 3].remove(ch)

        def backtrack(index):
            if index == len(empty_cells):
                return True
            row, col = empty_cells[index]
            for ch in '123456789':
                if is_valid(row, col, ch):
                    place_number(row, col, ch)
                    if backtrack(index + 1):
                        return True
                    remove_number(row, col, ch)
            return False
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]
        empty_cells = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                else:
                    place_number(i, j, board[i][j])

        backtrack(0)

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

sol = Solution()
sol.solveSudoku(board)

for row in board:
    print(row)

