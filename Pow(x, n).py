class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powbek(x, n):
            if n == 0:
                return 1.0
            elif n < 0:
                x = 1 / x
                n = -n

            if n % 2 == 0:
                half = powbek(x, n // 2)
                return half * half
            else:
                half = powbek(x, n // 2)
                return half * half * x

        return powbek(x, n)


sol = Solution()
print(sol.myPow(x = 2.00000, n = -2))