import random

def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


def generate_arr(n: int) -> list[int]:
    arr =[]
    for _ in range(n):
        arr.append(random.randint(-50, 50))
    return arr

n = int(input("Nechta taxminiy list elementlarini tartiblamoqchisiz:"))

arr = generate_arr(n)
print(f"Asl list:{arr}")
print(f"Tartiblangan list:{quicksort(arr)}")








