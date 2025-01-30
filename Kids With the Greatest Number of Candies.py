class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxcandies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies



sol= Solution()
print(sol.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))

