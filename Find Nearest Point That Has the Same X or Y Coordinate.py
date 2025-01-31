class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        mindist = float('inf')
        res = -1

        for i, (xi, yi) in enumerate(points):
            if xi != x and yi != y: continue
            curr_dist = abs(xi - x) + abs(yi - y)
            if curr_dist < mindist:
                mindist = curr_dist
                res = i

        return res



sol = Solution()
print(sol.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))