


def group_anagrams(strs: list[str]) -> list[list[str]]:

    anagaram_groups:dict[str, list[str]]= {}
    for word in strs:
        key = ''.join(sorted(word))

        if key in anagaram_groups:
            anagaram_groups[key].append(word)
        else:
            anagaram_groups[key] = [word]

    return list(anagaram_groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))