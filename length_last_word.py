def isSubsequence(s: str, t: str) -> bool:
    index_for_s, index_for_t = 0, 0
    while index_for_s < len(s) and index_for_t < len(t):
        if s[index_for_s] == t[index_for_t]:
            index_for_s += 1
        index_for_t += 1
    return index_for_s == len(s)

print(isSubsequence(s = "abc", t = "ahbgdc"))

