class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            print(ones)
            ones = (ones ^ num) & ~ twos
            print(twos)
            twos = (twos ^ num) & ~ ones
        return ones


sol = Solution()
print(sol.singleNumber(nums = [2, 2, 3, 2]))
