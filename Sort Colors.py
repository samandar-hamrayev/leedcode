class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, n - 1
        curr = 0
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1

sol = Solution()
print(sol.sortColors(nums = [2,0,2,1,1,0]))


