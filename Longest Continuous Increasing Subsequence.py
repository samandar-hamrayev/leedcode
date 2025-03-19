class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max_len = 0
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1
        max_len = max(max_len, cnt)
        return max_len



sol = Solution()
print(sol.findLengthOfLCIS(nums = [3]))
