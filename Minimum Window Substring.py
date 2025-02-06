from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = ''
        min_len = float('inf')
        t_count = Counter(t)
        s_count = {}
        required = len(t_count)
        formed = 0
        left = 0
        for right in range(len(s)):
            if s[right] in t_count:
                s_count[s[right]] = s_count.get(s[right], 0) + 1
                if s_count[s[right]] == t_count[s[right]]:
                    formed += 1

            while formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right+1]

                if s[left] in s_count:
                    s_count[s[left]] -= 1
                    if s_count[s[left]] < t_count[s[left]]:
                        formed -= 1
                left += 1


        return min_window

sol = Solution()
print(sol.minWindow(s = "a", t = "aa"))





