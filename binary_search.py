from random import randint
from time import perf_counter


def binary_search(nums: list[int], low: int, high: int, x: int):
    if high >= low:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid

        elif nums[mid] > x:
            return binary_search(nums, low, mid - 1, x)
        else:
            return binary_search(nums, mid + 1, high, x)
    else:
        return -1

arr = [randint(-10, 10) for _ in range(10)]
arr.sort()
print(arr)

x = int(input("x="))

result = binary_search(arr, 0, len(arr) - 1, x)

if result == -1:
    print("Arrayda bunday element yo'q")
else:
    print(result)