class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        natija = []
        word_set = set(wordDict)

        def ishchi(boshi:int, joriy: list[str]):
            if boshi == len(s):
                natija.append(" ".join(joriy))
                return

            for oxiri in range(boshi + 1, len(s) + 1):
                hozir = s[boshi:oxiri]
                if hozir in word_set:
                    joriy.append(hozir)
                    ishchi(oxiri, joriy)
                    joriy.pop()

        ishchi(0, [])
        return natija


sol = Solution()
print(sol.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))