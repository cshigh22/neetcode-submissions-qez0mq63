class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEndofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isEndofWord = True

    def search(self, word: str) -> bool:    
        def dfs(index, node):
            if index == len(word):
                return node.isEndofWord
                
            char = word[index]

            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                            return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
        return dfs(0, self.root)
