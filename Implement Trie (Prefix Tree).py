class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._searchPrefix(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self._searchPrefix(prefix)
        return node is not None

    def _searchPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return  node


trie = Trie()
print(trie.startsWith("a"))
