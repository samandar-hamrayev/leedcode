class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        start = 0

        for index in range(1, len(s)):
            if s[index] != s[index-1]:
                if index - start >= 3:
                    result.append([start, index-1])
                start = index
        if len(s) - start >= 3:
            result.append([start, len(s) - 1])
        return result

sol = Solution()
print(sol.largeGroupPositions(s = "abcdddeeeeaabbbcd"))








