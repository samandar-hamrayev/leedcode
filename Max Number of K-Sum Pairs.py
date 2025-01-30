class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            if nums[left] + nums[right] == k:
                nums.pop(left)
                nums.pop(right - 1)
                right -= 2
                operations += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return operations


solution = Solution()
print(solution.maxOperations(nums = [3,1,3,4,3], k = 6))


