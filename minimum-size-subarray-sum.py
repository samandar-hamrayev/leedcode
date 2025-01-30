def minSubArrayLen(target:int, nums: list[int]) -> int:
    n = len(nums)
    start = 0
    current_sum = 0
    min_length = float('inf')

    for end in range(n):
        current_sum += nums[end]

        while current_sum >= target:
            min_length = min(min_length, end - start +1)
            current_sum -= nums[start]
            start += 1

    return 0 if min_length == float('inf') else min_length


print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))