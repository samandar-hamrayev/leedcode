class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2

        match n % 3:
            case 0: return 3 ** (n // 3)
            case 1: return 3 ** (n // 3 - 1) * 4
            case 2: return 3 ** (n // 3) * 2

sol = Solution()
print(sol.integerBreak(2))


