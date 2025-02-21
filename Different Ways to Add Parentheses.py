from functools import lru_cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @lru_cache(None)
        def compute(expr: str):
            if expr.isdigit():
                return [int(expr)]
            res = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for l in left:
                        for r in right:
                            if ch == "+":
                                res.append(l + r)
                            elif ch == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)
            return res
        return compute(expression)

sol = Solution()
print(sol.diffWaysToCompute(expression = "2*3-4*5"))

