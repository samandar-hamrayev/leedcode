def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def worker(exness, comb, start):
        if exness == 0:
            result.append(list(comb))
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= exness:
                comb.append(candidates[i])
                worker(exness - candidates[i], comb, i)
                comb.pop()

    worker(target, [], 0)
    return result


print(combinationSum(candidates = [2,3,6,7], target = 7))