from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(words)

        for word, _ in count.most_common():
            if word not in banned:
                return word

sol = Solution()
print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
