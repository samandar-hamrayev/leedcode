class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left, target = 0, 0
        ziros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                ziros += 1

            while ziros > 1:
                if nums[left] == 0:
                    ziros -= 1
                left += 1

            target = max(target, right - left)
        return target

sol = Solution()
print(sol.longestSubarray(nums = [1,1,1,1,1,1,1,1]))



