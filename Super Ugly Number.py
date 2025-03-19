import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        primes_map = {p: 0 for p in primes}

        super_uglies = [1]

        for _ in range(n - 1):
            next_ugly, prime_val = min((super_uglies[v] * k, k) for k, v in primes_map.items())
            super_uglies.append(next_ugly)

            for k in primes_map:
                if next_ugly == super_uglies[primes_map[k]] * k:
                    primes_map[k] += 1

        return super_uglies[-1]



sol = Solution()
print(sol.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
