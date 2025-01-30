class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(start:int, comb:list[int], target: int):
            if len(comb) == k and target == 0:
                print(comb)
                result.append(comb[:])
                return

            if len(comb) > k or target < 0:
                print(comb)
                return

            for i in range(start, 10):
                comb.append(i)
                backtrack(i+1, comb, target - i)
                comb.pop()

        backtrack(1, [], n)
        return result


sol = Solution()
print(sol.combinationSum3(3, 9))

