class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEndofWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if node.children[idx] == None:
                return False
            node = node.children[idx]
        return node.isEndofWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            idx = ord(i) - ord('a')
            if node.children[idx] == None:
                return False
            node = node.children[idx]
        return True
        