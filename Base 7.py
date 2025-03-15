class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)

        result = ""
        while num > 0:
            result = str(num  % 7) + result
            num //= 7

        return "-" + result if is_negative else result

sol = Solution()
print(sol.convertToBase7(100))


