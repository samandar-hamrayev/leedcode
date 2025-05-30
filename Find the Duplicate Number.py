class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

sol = Solution()
print(sol.findDuplicate(nums = [3,3,3,3,3]))
