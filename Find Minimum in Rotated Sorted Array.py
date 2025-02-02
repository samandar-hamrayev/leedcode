class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]
sol = Solution()
print(sol.findMin(nums = [5,6,7,0,1,2,3,4]))