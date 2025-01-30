def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1


print(twoSum(numbers=[2, 3, 4], target=6))



# numbers = [2, 7, 11, 13, 15, 18, 21, 22, 25]