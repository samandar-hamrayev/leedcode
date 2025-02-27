class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        greater_map = {}
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            greater_map[num] = stack[-1] if stack else -1
            stack.append(num)
        return [greater_map[num] for num in nums1]

sol = Solution()
print(sol.nextGreaterElement(nums1 = [1], nums2 = [1]))
