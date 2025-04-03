class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:

        for row in  image:
            start, end = 0, len(row) - 1
            while start < end:
                row[end], row[start] = row[start] ^ 1, row[end] ^ 1
                start += 1
                end -= 1
            if start == end:
                row[start] ^= 1
        return image


sol = Solution()
print(sol.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))

print(1 ^ 1)