class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        prefix_sums = {0:0}
        summa = 0
        res = -float('inf')
        for i, num in enumerate(nums):
            summa += num
            mod = (i + 1) % k

            if mod in prefix_sums:
                res = max(res, summa - prefix_sums[mod])

            if mod not in prefix_sums or summa < prefix_sums[mod]:
                prefix_sums[mod] = summa
        return res



sol = Solution()
print(sol.maxSubarraySum(nums = [-1,-2,-3,-4,-5], k = 4))