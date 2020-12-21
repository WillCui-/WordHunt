import unittest
from src.trie import Trie
from collections import defaultdict

class TestTrie(unittest.TestCase):
    def test_init_type(self):
        trie = Trie()
        self.assertIsInstance(trie.root, defaultdict)

    def test_init_default_value(self):
        trie = Trie()
        self.assertEqual(trie.root['asdf'], '_end')
        self.assertEqual(trie.root[''], '_end')
        self.assertEqual(trie.root['123'], '_end')


if __name__ == '__main__':
    unittest.main()