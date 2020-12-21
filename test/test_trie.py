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


    def test_insert(self):
        trie = Trie()
        trie.insert('hello')
        root = trie.root
        self.assertEqual(root['a'], '_end')
        self.assertIsInstance(root['a'], str)
        self.assertIsInstance(root['h'], defaultdict)

        subroot = root['h']

        self.assertEqual(subroot['a'], '_end')


    def test_search(self):
        trie = Trie()
        trie.insert('hello')
        self.assertTrue(trie.search('hello'))
        self.assertFalse(trie.search('hel'))
        self.assertFalse(trie.search('bla'))


    def test_starts(self):
        trie = Trie()
        trie.insert('hello')
        self.assertTrue(trie.starts('hello'))
        self.assertTrue(trie.starts('hel'))
        self.assertFalse(trie.starts('hello!'))
