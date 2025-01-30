class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(comb: list[int], start: int):
            if len(comb) == k:
                result.append(list(comb))
                return

            for i in range(start, n - (k - len(comb)) + 2):
                comb.append(i)
                backtrack(comb, i + 1)
                comb.pop()
        backtrack([], 1)
        return result


solution = Solution()
print(solution.combine(5,3))
