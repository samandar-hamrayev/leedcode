class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result



sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))