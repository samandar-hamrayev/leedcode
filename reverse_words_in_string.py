def reverseWords(s: str) -> str:
    return " ".join([word for word in s.split()][::-1])

print(reverseWords(s = "what the fuck is that     "))
