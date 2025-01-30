class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        result = []
        def is_palindrome(sub):
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start:int, path:list[str]):
            if start == n:
                result.append(path[:])
                return

            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return result



sol = Solution()
print(sol.partition('aa'))


