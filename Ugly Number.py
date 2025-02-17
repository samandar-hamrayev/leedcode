class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for checker in [2, 3, 5]:
            while n % checker == 0:
                n //= checker
        return n == 1

sol = Solution()
print(sol.isUgly(6))
