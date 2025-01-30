class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        def backtrack(start:int, path:list[str]):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return

            for i in range(1, 4):
                if start + i > len(s):
                    break
                segm = s[start:start + i]
                print(segm)

                if (segm[0] == '0' and len(segm) > 1) or int(segm) > 255:
                    continue
                backtrack(start+i, path + [segm])
        backtrack(0, [])
        return result

sol = Solution()
print(sol.restoreIpAddresses('25525511135'))




