class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold, cash = -prices[0], 0
        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash,  hold + price - fee)
        return cash

sol = Solution()
print(sol.maxProfit(prices = [1,5,7,5,10,3], fee = 3))
