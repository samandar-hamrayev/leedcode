class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(set(nums)) > 2:
            return sorted(nums)[-3]
        else:
            return max(nums)



sol =  Solution()
print(sol.thirdMax([2,2,3,1, 7, 3, 8, 7, 1, 90, 76]))



