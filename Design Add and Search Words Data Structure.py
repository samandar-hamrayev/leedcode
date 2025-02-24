class TrieNode:
    def __init__(self):
        self.children  = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node: TrieNode, word: str, index: int):
        if len(word) == index:
            return node.is_end_of_word

        ch = word[index]

        if ch == '.':
            for child in node.children.values():
                if self._dfs(child, word, index+1):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self._dfs(node.children[ch], word, index+1)

# ✅ Foydalanish usuli:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))  # ❌ False
print(obj.search("bad"))  # ✅ True
print(obj.search(".ad"))  # ✅ True
print(obj.search("b.."))  # ✅ True