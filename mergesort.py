def mergesort(nums: list[int]):
    if len(nums) >  1:
        mid = len(nums) // 2

        left = mergesort(nums[:mid])
        right = mergesort(nums[mid:])
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return nums


print(mergesort([5, 7, 3, 9, 10, 2]))



