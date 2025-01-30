from typing import List


def canJump(nums: List[int]) -> bool:
    max_reach = 0
    n = len(nums)

    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

        if max_reach >= n - 1:
            return True

    return False
nums = [3, 2, 1, 0, 4, 3, 2, 0, 4]
print(canJump(nums))

