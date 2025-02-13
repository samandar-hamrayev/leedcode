class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1: return

        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]: i -= 1

        if i >= 0:
            j = n - 1
            while nums[i] >= nums[j]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])

sol = Solution()
sol.nextPermutation(nums = [1,2,3])

