class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stc = []

        for astroid in asteroids:
            if astroid > 0:
                stc.append(astroid)
            else:
                while stc and stc[-1] > 0:
                    if stc[-1] == abs(astroid):
                        stc.pop()
                        break
                    elif stc[-1] < abs(astroid):
                        stc.pop()
                    else:
                        break
                else:
                    stc.append(astroid)
        return stc


# sol = Solution()
# print(sol.asteroidCollision([10, 2, -5]))




