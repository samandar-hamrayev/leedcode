class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        return [num for num in set(nums2) if num in set1]


solution = Solution()
print(solution.intersection(nums1 = [1,2,2,1,5], nums2 = [2,2,5]))
