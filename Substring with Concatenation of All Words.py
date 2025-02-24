from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        res = []
        total_length, s_length = len(words) * len(words[0]), len(s)
        word_length = len(words[0])

        if total_length > s_length:
            return []

        word_mp = Counter(words)

        for i in range(word_length):
            left, right = i, i
            current_mp = Counter()
            count = 0

            while right + word_length <= s_length:
                word = s[right:right+word_length]
                right += word_length

                if word in word_mp:
                    current_mp[word] += 1
                    count += 1

                    while current_mp[word] > word_mp[word]:
                        left_word = s[left:left+word_length]
                        current_mp[left_word] -= 1
                        count -= 1
                        left += word_length

                    if count == len(words):
                        res.append(left)

                else:
                    current_mp.clear()
                    count = 0
                    left = right
        return res

sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))  # Output: [0,9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # Output: []
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # Output: [6,9,12]






