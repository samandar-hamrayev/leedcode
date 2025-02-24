class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        max_val, min_val = max(nums), min(nums)

        count = [0] * (max_val - min_val + 1)
        for num in nums:
            count[num - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        sorted_arr = [0] * len(nums)
        for num in reversed(nums):
            sorted_arr[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
        print(sorted_arr)
        return sum(sorted_arr[::2])
sol = Solution()
print(sol.arrayPairSum(nums = [1, 4, 3, 2]))