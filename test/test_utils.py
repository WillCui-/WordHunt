import unittest
from src.utils import serialize, deserialize
from src.trie import Trie

class TestUtils(unittest.TestCase):
    def test_serialize_deserialize(self):
        trie = Trie()
        trie.insert('h')
        trie.insert('hh')
        trie.insert('he')
        ser = serialize(trie.root)

        self.assertEqual(len(ser), 14)

        de = deserialize(serialize(trie.root))
        self.assertIsInstance(de, Trie)
        self.assertEqual(trie.root.keys(), de.root.keys())
        self.assertEqual(trie.root['h'].keys(), de.root['h'].keys())
        

    def test_serialize_deserialize_different_prefixes(self):
        trie = Trie()
        trie.insert('a')
        trie.insert('bc')
        trie.insert('de')
        ser = serialize(trie.root)

        self.assertEqual(len(ser), 20)

        de = deserialize(serialize(trie.root))
        self.assertIsInstance(de, Trie)
        self.assertEqual(trie.root.keys(), de.root.keys())
        self.assertEqual(trie.root['a'].keys(), de.root['a'].keys())


    def test_serialize_deserialize_duplicates(self):
        trie = Trie()
        trie.insert('a')
        trie.insert('bc')
        trie.insert('de')
        trie.insert('bc')
        ser = serialize(trie.root)

        self.assertEqual(len(ser), 20)

        de = deserialize(serialize(trie.root))
        self.assertIsInstance(de, Trie)
        self.assertEqual(trie.root.keys(), de.root.keys())
        self.assertEqual(trie.root['a'].keys(), de.root['a'].keys())


    def test_serialize_deserialize_prefix_words(self):
        trie = Trie()
        trie.insert('a')
        trie.insert('abc')
        trie.insert('abcde')
        trie.insert('abcdefg')
        ser = serialize(trie.root)

        self.assertEqual(len(ser), 27)

        de = deserialize(serialize(trie.root))
        self.assertIsInstance(de, Trie)
        self.assertEqual(trie.root.keys(), de.root.keys())
        self.assertEqual(trie.root['a'].keys(), de.root['a'].keys())