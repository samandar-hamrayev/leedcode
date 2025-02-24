class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = len(list(filter(lambda x: x.isupper(), word)))
        return len(word) == capitals or capitals == 1 and word[0].isupper() or capitals == 0
