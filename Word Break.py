class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        print(dp)
        return dp[n]


sol = Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet","code"]))


