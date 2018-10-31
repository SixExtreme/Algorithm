class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.is_word = True

    def search(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.is_word

    def startWith(self, prefix):
        root = self.root
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return True


