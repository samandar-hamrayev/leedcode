from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = Counter([tuple(row) for row in grid])
        cols = Counter([tuple(col) for col in zip(*grid)])

        mapping = {}
        for key in rows.keys() &  cols.keys():
            mapping[key] = rows[key] * cols[key]

        return sum(mapping.values())

sol = Solution()
print(sol.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))





