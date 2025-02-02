from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_count = Counter(chars)
        res = 0
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= char_count[c] for c in word_count):
                res += len(word)
        return res

sol = Solution()
print(sol.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))