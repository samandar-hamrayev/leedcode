class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        prev2, prev1 = 0, nums[0]
        for i in range(1, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current
        return prev1
sol = Solution()
print(sol.rob(nums = [2,1, 1,2]))

