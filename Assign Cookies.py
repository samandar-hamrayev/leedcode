class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        total = 0

        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                total += 1
                i += 1
                j += 1
            else:
                j += 1
        return total

sol = Solution()
print(sol.findContentChildren(g = [1,2], s = [1,2,3]))

