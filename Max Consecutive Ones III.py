class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, maxsize = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            maxsize = max(maxsize, right - left + 1)
        return maxsize
sol = Solution()
print(sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))





