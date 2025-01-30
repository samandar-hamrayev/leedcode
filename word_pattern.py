def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()

    mapP = {}
    mapW = {}

    for p, w in zip(pattern, words):
        if p in mapP and mapP[p] != w:
            return False

        if w in mapW and mapW[w] != p:
            return False

        else:
            mapP[p] = w
            mapW[w] = p
    return  True


print(wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
