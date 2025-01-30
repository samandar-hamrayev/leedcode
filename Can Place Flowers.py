class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

        return count >= n


sol = Solution()
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))



