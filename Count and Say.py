class Solution:
    def countAndSay(self, n: int) -> str:
        base_state = "1"
        for _ in range(n - 1):
            base_state = self.helper(base_state)
        return base_state

    def helper(self, text: str) -> str:
        count = 1
        res = ""
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                res += str(count) + text[i - 1]
                count = 1
        res += str(count) + text[-1]
        return res


sol = Solution()
# print(sol.countAndSay(4))
print(sol.helper('1'))

