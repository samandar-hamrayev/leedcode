def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Harf sanash uchun hash table (dictionary) yaratish
    s_count = {}
    t_count = {}

    # Birinchi stringdagi harf va takrorlanishlarini sanab chiqing
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1

    # Ikkinchi stringdagi harf va takrorlanishlarini sanab chiqing
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Ikkala dictionaryni taqqoslash
    return s_count == t_count

# Misollarni sinab ko'rish
print(isAnagram('rat', 'car'))  # Output: False
print(isAnagram('listen', 'silent'))  # Output: True