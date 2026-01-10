class Solution:
    @staticmethod
    def can_make_square(grid: list[list[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                colors = [
                    grid[i][j],
                    grid[i][j + 1],
                    grid[i + 1][j],
                    grid[i + 1][j + 1]
                ]
                black_count = colors.count('B')
                white_count = colors.count('W')
                if black_count >= 4 or white_count >= 4:
                    print(colors)
                    return True

        return False


solution = Solution()
print(solution.can_make_square([["B","W","B"],["B","W","W"],["B","B","B"]]))

