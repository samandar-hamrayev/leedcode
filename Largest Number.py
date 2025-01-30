class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        str_nums = list(map(str, nums))
        str_nums.sort(key=lambda s: s*10, reverse=True)
        return ''.join(str_nums) if str_nums[0] != "0" else "0"






sol = Solution()
print(sol.largestNumber(nums = [3,30,34,5,9,0]))