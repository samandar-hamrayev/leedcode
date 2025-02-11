class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res = (res + ord(columnTitle[i]) - ord('A') + 1)
            if i != len(columnTitle) - 1:
                res = res * 26
        return res

sol = Solution()
print(sol.titleToNumber('NTP'))


