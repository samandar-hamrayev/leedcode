class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        ans = [0] * n

        moves, count = 0, 0
        for i in range(n):
            ans[i] = moves
            count += int(boxes[i])
            moves += count

        moves, count = 0, 0
        for i in range(n-1, -1, -1):
            ans[i] += moves
            count += int(boxes[i])
            moves += count

        return ans

sol = Solution()
print(sol.minOperations(boxes = "001011"))
