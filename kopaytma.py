n = int(input())
count = 0
nums = [i for i in range(-abs(n), abs(n) + 1)]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] * nums[j] == n:
            count +=1
            print(f"{nums[i]}, {nums[j]}")

print(count)
