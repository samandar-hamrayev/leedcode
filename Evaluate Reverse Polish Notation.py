class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        for ch in tokens:
            if ch in operations:
                last1, last2 = stack.pop(), stack.pop()
                stack.append(operations[ch](last2, last1))
            else:
                stack.append(int(ch))

        return stack[0]

sol = Solution()
print(sol.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

