class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')

        res = []
        for word in words:
            if (
                    all(ch in set1 for ch in word.lower()) or
                    all(ch in set2 for ch in word.lower()) or
                    all(ch in set3 for ch in word.lower())
            ):
                res.append(word)
        return res


sol = Solution()
print(sol.findWords(words = ["Hello","Alaska","Dad","Peace"]))
