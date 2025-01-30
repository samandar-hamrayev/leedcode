class Solution:
    def missingNumber1th(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == m:
                l = m + 1
            else:
                r = m - 1
        else:
            return l


    def missingNumber2th(self, nums: list[int]) -> int:
        sum = len(nums) * (1 + len(nums)) / 2
        act_sum = 0
        for num in nums:
            act_sum += num
        return sum - act_sum


solution = Solution()
print(solution.missingNumber1th([3, 0, 2, 1]))
print(solution.missingNumber2th([3, 0, 2, 1]))
