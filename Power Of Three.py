class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def f(n):
            if n < 1:
                return False
            if n == 1:
                return True

            if n % 3 == 0: return f(n // 3)
            else: return False

        return f(n)

sol = Solution()
print(sol.isPowerOfThree(9))