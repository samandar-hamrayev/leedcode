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



def quicksort(arr : list[int]):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [num for num in arr[1:] if num < pivot]
        right = [num for num in arr[1:] if num >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

print(mergesort([4, 2,7, 3, 2, 9, 4]))
print(quicksort([4, 2,7, 3, 2, 9, 4]))



