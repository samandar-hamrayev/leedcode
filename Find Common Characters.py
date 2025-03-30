from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        char_counts = [Counter(word) for word in words]

        common_freq = char_counts[0]
        for char_count in char_counts[1:]:
            for char in list(common_freq.keys()):
                if char in char_count:
                    common_freq[char] = min(common_freq[char], char_count[char])
                else:
                    del common_freq[char]

        res = []
        for char, freq in common_freq.items():
            res.extend([char] * freq)

        return res


# Test case
sol = Solution()
print(sol.commonChars(["bella", "label", "roller"]))  # Output: ['e', 'l', 'l']

