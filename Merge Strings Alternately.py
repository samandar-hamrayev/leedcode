class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        index = 0
        while index < len(word1) and index < len(word2):
            result += word1[index] + word2[index]
            index += 1

        if index <= len(word1):
            result += word1[index:]


        if index <= len(word2):
            result += word2[index:]

        return result


soltion = Solution()
print(soltion.mergeAlternately(word1 = "abcd", word2 = "pq"))
