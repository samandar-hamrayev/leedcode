from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        mp = Counter(digits)
        result = []
        for number in range(100, 1000, 2):
            a, b, c = self.worker(number)
            number_counter = Counter([a, b, c])
            if all(mp[d] >= number_counter[d] for d in number_counter):
                result.append(number)
        return sorted(result)

    def worker(self, number):
        return number // 100, (number % 100) // 10, number % 10
