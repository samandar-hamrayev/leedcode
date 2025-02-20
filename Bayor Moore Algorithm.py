class BayorMoore:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.bad_char_table = self._preprocess_bad_character()

    def _preprocess_bad_character(self):
        m = len(self.pattern)
        table = {}
        for i in range(m-1):
            table[self.pattern[i]] = i
        return table

    def search(self, txt: str):
        m, n = len(self.pattern), len(txt)
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and self.pattern[j] == txt[i+j]:
                j -= 1
            if j < 0:
                return i

            bad_char_shift = j - self.bad_char_table.get(txt[i+j], -1)
            i += max(bad_char_shift, 1)
        return -1



obj = BayorMoore('ABC')
print(obj.search("ABAABCA"))



