class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum


sol = Solution()
print(sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))