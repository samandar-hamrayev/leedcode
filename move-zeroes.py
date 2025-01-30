def moveZeroes(nums: list[int]):
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            n -= 1
        else:
            i += 1

    print(nums)


moveZeroes(nums = [0, 0])

