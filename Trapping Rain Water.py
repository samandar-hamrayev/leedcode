class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        lmax, rmax = 0, height[right]
        total = 0

        while left < right:
            if height[left] < height[right]:
                if lmax >= height[left]:
                    total += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1

            else:
                if rmax > height[right]:
                    total += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1
        return total


sol = Solution()
print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))

