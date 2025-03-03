from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum( s == g for s, g in zip(secret, guess))
        s_c, g_c = Counter(secret), Counter(guess)
        cows = sum(min(s_c[ch], g_c[ch]) for ch in g_c if ch in s_c) - bulls
        return f"{bulls}A{cows}B"

sol = Solution()
print(sol.getHint(secret = "1807", guess = "7810"))
