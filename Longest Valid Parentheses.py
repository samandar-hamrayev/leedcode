class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stc = [-1]
        maks = 0
        for i in range(len(s)):
            if s[i] == "(":
                stc.append(i)
            else:
                stc.pop()
                if not stc:
                    stc.append(i)
                else:
                    maks = max(maks, i - stc[-1])
        return maks


sol = Solution()
print(sol.longestValidParentheses("()(()"))