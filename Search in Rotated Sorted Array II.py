class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True

            if nums[l] == nums[r] == nums[m]:
                l += 1
                r -= 1
                continue

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False

sol = Solution()
print(sol.search(nums = [3, 1], target = 1))

