
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        nums = []
        l, t, r, b = 0, 0, len(matrix[0]) - 1, len(matrix) -1

        while l <= r and t <= b:
            for i in range(l, r+1):
                nums.append(matrix[t][i])
            t += 1

            for i in range(t, b+1):
                nums.append(matrix[i][r])
            r -=1

            if t <= b:
                for i in range(r, l-1, -1):
                    nums.append(matrix[b][i])
                b -=1

            if l <= r:
                for i in range(b, t-1, -1):
                    nums.append(matrix[i][ l])
                l +=1
            print(nums)
        return nums


sol = Solution()
print(sol.spiralOrder([[1,2,3,4],
                       [5,6,7,8],
                       [9,10,11,12],
                       [13,14,15,16],
                       [17,18,19,20],
                       [21,22,23,24]]))




