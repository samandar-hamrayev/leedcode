def canConstruct(ransomNote:str, magazine: str) -> bool:
    ransom_counts = {}
    for char in ransomNote:
        if char in ransom_counts:
            ransom_counts[char] += 1
        else:
            ransom_counts[char] = 1

    for char, count in ransom_counts.items():
        if magazine.count(char) < count:
            return False
    return True


print(canConstruct(ransomNote = "aa", magazine = "aab"))
