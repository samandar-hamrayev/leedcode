class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        if letters[-1] <= target:
            return letters[0]

        while l < r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l]









