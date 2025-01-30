def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    pref = 1
    for i in range(n):
        result[i] = pref
        pref *= nums[i]

    suff = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suff
        suff *= nums[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))


