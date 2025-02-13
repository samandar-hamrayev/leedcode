class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1l, s2l, s3l = len(s1), len(s2), len(s3)
        if s1l + s2l != s3l:
            return False

        dp = [False] * (s2l + 1)
        dp[0] = True

        for j in range(1, s2l + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, s1l + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, s2l + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1]

sol = Solution()
print(sol.isInterleave("abcd", "aadde", "aadadbcde"))
