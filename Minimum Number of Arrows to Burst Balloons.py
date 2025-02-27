class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda lst: lst[1])
        shots = 1
        left = points[0]
        i = 1
        while i < len(points):
            if left[1] < points[i][0]:
                shots += 1
                left = points[i]
            i += 1
        return shots

sol = Solution()
print(sol.findMinArrowShots(points = [[10,16], [17, 19]]))
