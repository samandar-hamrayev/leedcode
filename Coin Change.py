class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0]=0

        for summa in range(1, amount + 1):
            for coin in coins:
                if summa >= coin:
                    dp[summa] = min(dp[summa],dp[summa-coin] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]


sol = Solution()
print(sol.coinChange(coins = [1], amount = 0))

