import math
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        for w in range(int(math.sqrt(area)), 0, -1):
            if area % w == 0:
                return [area // w, w]


sol = Solution()
print(sol.constructRectangle(1))



