class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(opens, closes, s):
            if opens == closes and opens + closes == 2 * n:
                result.append(s)
                print(s)
                return

            if opens < n:
                backtrack(opens + 1, closes, s + "(")

            if closes < opens:
                backtrack(opens, closes + 1, s + ")")

        backtrack(0, 0, "")
        return result


sol = Solution()
print(sol.generateParenthesis(3))
