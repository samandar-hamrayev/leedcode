class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1, n2 = len(version1), len(version2)
        v1, v2 = 0, 0
        while v1 < n1 or v2 < n2:
            sub_v1, sub_v2 = 0, 0
            while v1 < n1 and version1[v1] != ".":
                sub_v1 = sub_v1 * 10 + int(version1[v1])
                v1 += 1

            while v2 < n2 and version2[v2] != ".":
                sub_v2 = sub_v2 * 10 + int(version2[v2])
                v2 += 1

            if sub_v1 > sub_v2:
                return  1
            elif sub_v1 < sub_v2:
                return -1
            v1 += 1
            v2 += 1
        return 0




sol = Solution()
print(sol.compareVersion(version1 = "1.2", version2 = "1.10"))



