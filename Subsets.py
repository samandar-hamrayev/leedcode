class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        def backer(comb:list[int], start:int):
            result.append(list(comb))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                comb.append(nums[i])
                backer(comb, i + 1)
                comb.pop()

        backer([], 0)
        return result


sol = Solution()
print(sol.subsets([4,4,4,1,4]))


