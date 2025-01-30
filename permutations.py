def permute(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    def worker(little, unused):
        if not unused:
            result.append(little)

        for i in range(len(unused)):
            if i > 0 and unused[i] == unused[i-1]:
                continue
            worker(little + [unused[i]], unused[:i] + unused[i+1:])

    worker([], nums)
    return result

print(permute([3,3,0,3]))