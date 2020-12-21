from collections import defaultdict

class Trie():
    """
    Initialization
    """
    def __init__(self):
        self.root = defaultdict(lambda: "_end")


    """
    Inserts word into Trie and returns the Trie
    """
    def insert(self, word):
        root = self.root

        for letter in word:
            root = root.setdefault(letter, defaultdict(lambda: "_end"))
        root["_end"] = "_end"
        return self.root

    """
    Returns True if word is in Trie, False if not
    """
    def search(self, word):
        root = self.root

        for letter in word:
            if letter not in root:
                return False
            root = root[letter]

        if "_end" in root:
            return True

        return False


    """
    Returns True if prefix is in Trie, False if not
    """
    def starts(self, word):
        root = self.root

        for letter in word:
            if letter not in root:
                return False
            root = root[letter]

        return True