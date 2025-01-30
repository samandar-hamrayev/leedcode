class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        col, row = len(board), len(board[0])

        def dfs(c, r, idx):
            if idx == len(word):
                return True
            if c < 0 or c >= col or r < 0 or r >= row or word[idx] != board[c][r]:
                return False

            seen = board[c][r]
            board[c][r] = "#"
            res = (
                dfs(c + 1, r, idx + 1) or
                dfs(c - 1, r, idx + 1) or
                dfs(c, r + 1, idx + 1) or
                dfs(c, r - 1, idx + 1)
            )
            board[c][r] = seen
            return res
        for i in range(col):
            for j in range(row):
                if dfs(i, j, 0):
                    return True
        return False


sol = Solution()
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
