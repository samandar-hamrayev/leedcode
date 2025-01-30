def isIsomorphic(s: str, t: str) ->bool:
    n = len(s)
    s_map = {}

    for i in range(n):
        if s[i] in s_map:
            if s_map[s[i]] != t[i]:
                return False
        else:
            if t[i] not in s_map.values():
                s_map[s[i]] = t[i]
            else:
                return False

    return True

print(isIsomorphic(s = "badc", t = "baba"))

