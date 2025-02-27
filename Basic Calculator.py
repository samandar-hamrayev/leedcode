class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, res, sign = 0, 0, 1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "-+":
                res += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")":
                res += num * sign
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + sign * num


sol = Solution()
print(sol.calculate(s = "2147483647"))
