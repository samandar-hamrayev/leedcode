class Solution:
    def calculate(self, s: str) -> int:
        s += "+"
        stack = []
        num = 0
        op = "+"

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                match op:
                    case "+":
                        stack.append(num)
                    case "-":
                        stack.append(-num)
                    case "*":
                        stack.append(stack.pop() * num)
                    case "/":
                        stack.append(int(stack.pop() / num))
                op = ch
                num = 0

        return sum(stack)


sol = Solution()
print(sol.calculate("3+5/2*3"))  # 5
