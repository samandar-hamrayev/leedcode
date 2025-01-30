class Solution:
    def count_vowel(self, word):
        res = 0
        for char in word:
            if char in ['a', 'e', 'i', 'o', 'u']:
                res += 1
        return res

    def maxVowels(self, s: str, k: int) -> int:
        target = -float('inf')
        for i in range(len(s) - k + 1):
            word = s[i:i+k]
            target = max(target, self.count_vowel(word))
            if target == k:
                return target
        return target

solution = Solution()

print(solution.maxVowels(s = "abciiidef", k = 3))


