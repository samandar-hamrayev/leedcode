class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_sub = 0
        start = 0
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        start = i
        while i < len(nums):
            if nums[i] == 0:
                max_sub = max(max_sub, i - start)
                while i < len(nums) and nums[i] == 0:
                    i += 1
                start = i
            else:
                i += 1
        max_sub = max(max_sub, i - start)
        return max_sub

sol = Solution()
print(sol.findMaxConsecutiveOnes([0, 1]))