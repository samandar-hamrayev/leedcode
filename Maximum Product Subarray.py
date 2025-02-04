
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currmax = currmin = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                currmax, currmin = currmin, currmax

            currmax = max(num, currmax * num)
            currmin = min(num, currmin * num)

            result = max(result, currmax)

        return result

sol = Solution()
print(sol.maxProduct(nums=[2, 3, 4, 6]))


