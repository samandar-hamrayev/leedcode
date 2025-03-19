class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()

        first_group_len = len(s) % k

        res = s[:first_group_len]

        for i in range(first_group_len, len(s), k):
            if res:
                res += '-'
            res += s[i:i + k]

        return res

sol = Solution()
print(sol.licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))  # Output: "5F3Z-2E9W"
print(sol.licenseKeyFormatting(s="2-5g-3-J", k=2))     # Output: "2-5G-3J"
