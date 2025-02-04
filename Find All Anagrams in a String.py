class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        res = []
        p_count = [0] * 26
        s_count = [0] * 26
        a_ord = ord('a')

        for ch in p:
            p_count[ord(ch) - a_ord] += 1

        for i in range(len(p)):
            s_count[ord(s[i]) - a_ord] += 1

        if s_count == p_count:
            res.append(0)

        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - a_ord] += 1
            s_count[ord(s[i - len(p)]) - a_ord] -= 1

            if s_count == p_count:
                res.append(i - len(p) + 1)

        return res


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
print(sol.findAnagrams("abab", "ab"))