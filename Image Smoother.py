from math import floor


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        smoothed_img = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt,local_sum = 0, 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            local_sum += img[ni][nj]
                            cnt += 1
                smoothed_img[i][j] = local_sum // cnt
        return smoothed_img



sol = Solution()
print(sol.imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]]))
