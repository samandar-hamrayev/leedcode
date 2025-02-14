from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = Counter(s)
        ans = 0
        odd_found = False
        for cnt in mp.values():
            ans += cnt // 2 * 2
            if cnt % 2 != 0:
                odd_fount = True
        return ans + int(odd_found)


sol = Solution()
print(sol.longestPalindrome('abccccdd'))