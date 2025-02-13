class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)

        for node in range(2, n + 1):
            left, right, total = 0, node - 1, 0
            while left <= right:
                if left == right:
                    total += dp[left] * dp[right]
                else:
                    total += 2 * dp[left] * dp[right]
                left += 1
                right -= 1
            dp[node] = total
        return dp[n]


sol = Solution()
print(sol.numTrees(4))
