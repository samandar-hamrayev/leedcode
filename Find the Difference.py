class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # sum_ords_s = 0
        # sum_ords_t = 0
        # for ch in s:
        #     sum_ords_s += (ord(ch) - ord("A"))
        #
        # for ch in t:
        #     sum_ords_t += (ord(ch) - ord("A"))

        # return chr(sum_ords_t - sum_ords_s + ord("A"))

        return chr(sum(map(ord, t)) - sum(map(ord, s)))


sol = Solution()
print(sol.findTheDifference(s = "", t = "y"))
