class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(excess: int, comb:list[int], start: int):
            if excess == 0:
                result.append(list(comb))
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] <= excess:
                    comb.append(candidates[i])
                    backtrack(excess - candidates[i], comb, i + 1)
                    comb.pop()

        backtrack(target, [], 0)
        return result



sol = Solution()
print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))