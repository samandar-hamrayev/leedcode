class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > num:
                right = mid - 1
            elif mid ** 2 < num:
                left = mid + 1
            else:
                return mid
        else:
            return left - 1

solution = Solution()
print(solution.isPerfectSquare(144))