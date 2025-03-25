class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()

        return " ".join(
            (word + "ma" + "a" * (i + 1)) if word[0] in vowels
            else (word[1:] + word[0] + "ma" + "a" * (i + 1))
            for i, word in enumerate(words)
        )




sol = Solution()
print(sol.toGoatLatin(sentence = "I speak Goat Latin"))