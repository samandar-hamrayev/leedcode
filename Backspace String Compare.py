class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_valid_index(string, idx):
            backspace_count = 0
            while idx >= 0:
                if string[idx] == "#":
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                idx -= 1
            return idx

        s_idx, t_idx = len(s) - 1, len(t) - 1

        while s_idx >= 0 or t_idx >= 0:
            s_idx = get_next_valid_index(s, s_idx)
            t_idx = get_next_valid_index(t, t_idx)

            if s_idx >= 0 and t_idx >= 0:
                if s[s_idx] != t[t_idx]:
                    return False

            elif s_idx >= 0 or t_idx >= 0:
                return False

            s_idx -= 1
            t_idx -= 1

        return True


sol = Solution()
print(sol.backspaceCompare(s = "ab#c", t = "ad#c"))