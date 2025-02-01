# from functools import  lru_cache
#
# class Solution:
#     def numSquares(self, n: int) -> int:
#         @lru_cache(None)
#         def dfs(exness):
#             if exness == 0:
#                 return 0
#             if exness < 0:
#                 return float('inf')
#             min_steps = exness
#             current_num = 1
#             while current_num ** 2 <= exness:
#                 min_steps = min(min_steps, 1 + dfs(exness - current_num ** 2))
#                 current_num += 1
#             return min_steps
#         return dfs(n)
#
#
# sol = Solution()
# print(sol.numSquares(9)

